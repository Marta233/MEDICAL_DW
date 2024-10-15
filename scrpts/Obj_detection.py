import torch
import os
import pandas as pd
import shutil
import psycopg2
from datetime import datetime

class YOLOv5Detector:
    def __init__(self, model_name='yolov5s', base_output_folder='./YOLO_output'):
        self.model = self.load_model(model_name)
        self.base_output_folder = base_output_folder
        os.makedirs(self.base_output_folder, exist_ok=True)
        self.conn = self.connect_to_db()
        self.create_table_if_not_exists()

    # Load YOLO model
    def load_model(self, model_name):
        print(f"Loading YOLOv5 model: {model_name}")
        return torch.hub.load('ultralytics/yolov5', model_name)

    # Connect to PostgreSQL database using environment variables
    def connect_to_db(self):
        db_params = {
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }
        return psycopg2.connect(**db_params)

    # Create a table if it doesn't exist
    def create_table_if_not_exists(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS detections (
            id SERIAL PRIMARY KEY,
            img_name VARCHAR(255),
            name VARCHAR(255),
            confidence FLOAT,
            xmin_coord FLOAT,
            ymin FLOAT,
            xmax_coord FLOAT,
            ymax FLOAT,
            image_path VARCHAR(255),
            detection_time TIMESTAMP
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(create_table_query)
            self.conn.commit()
        print("Table 'detections' created or exists already.")

    # Run object detection and process images
    def detect_objects_in_images(self, image_folder):
        all_detections = []
        for img_name in os.listdir(image_folder):
            img_path = os.path.join(image_folder, img_name)
            
            # Run object detection
            results = self.model(img_path)
            results.save()  # Save detected images in './runs/detect/exp'

            # Handle YOLO temp folders (find latest)
            base_temp_folder = './runs/detect/'
            latest_exp_folder = max([os.path.join(base_temp_folder, d) for d in os.listdir(base_temp_folder)], key=os.path.getmtime)
            detected_img_path = os.path.join(latest_exp_folder, img_name)

            # Move detected images to the final output folder
            new_img_path = os.path.join(self.base_output_folder, img_name)
            if os.path.exists(detected_img_path):
                shutil.move(detected_img_path, new_img_path)
            else:
                print(f"Error: Detected image for {img_name} not found in {latest_exp_folder}")
                continue

            # Extract detection results
            detections = results.pandas().xyxy[0]
            detections['img_name'] = img_name
            detections['image_path'] = new_img_path
            detections['detection_time'] = datetime.now()  # Adding timestamp for detection

            all_detections.append(detections)

            print(f"Processed {img_name} and moved detected image to {new_img_path}")
        
        # Concatenate all detections into a single DataFrame
        return pd.concat(all_detections, ignore_index=True)

    # Insert detection data into PostgreSQL
    def insert_detections_to_db(self, detections_df):
        insert_query = """
        INSERT INTO detections (img_name, name, confidence, xmin_coord, ymin, xmax_coord, ymax, image_path, detection_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        with self.conn.cursor() as cur:
            for _, row in detections_df.iterrows():
                cur.execute(insert_query, (
                    row['img_name'], row['name'], row['confidence'], 
                    row['xmin'], row['ymin'], row['xmax'], row['ymax'],
                    row['image_path'], row['detection_time']
                ))
            self.conn.commit()
        print("Data inserted into PostgreSQL.")
    # Save detection results to CSV
    def save_to_csv(self, detections_df, csv_name='all_images_detections.csv'):
        csv_output_path = os.path.join(self.base_output_folder, csv_name)
        detections_df[['img_name', 'name', 'confidence', 'xmin', 'ymin', 'xmax', 'ymax']].to_csv(csv_output_path, index=False)
        print(f"Saved all detections to {csv_output_path}")
        return csv_output_path




