{{ config(materialized='table') }} -- Materialize the model as a table for optimized storage and querying

WITH transformed_detection AS (
    -- Correctly reference the 'detections' table using 'source'
    SELECT 
        id,
        img_name,
        name,
        confidence,
        xmin_coord,
        ymin,
        xmax_coord,
        ymax,
        image_path,
        detection_time,
        -- Extract the year, month, and day from the detection_time
        EXTRACT(YEAR FROM detection_time) AS detection_year,
        EXTRACT(MONTH FROM detection_time) AS detection_month,
        EXTRACT(DAY FROM detection_time) AS detection_day
    FROM {{ source('public', 'detections') }}  -- Source reference for the detections table
)

SELECT *
FROM transformed_detection;
