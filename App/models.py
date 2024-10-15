from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class Detection(Base):
    __tablename__ = "detections"
    
    id = Column(Integer, primary_key=True, index=True)
    img_name = Column(String(255), index=True)
    name = Column(String(255))
    confidence = Column(Float)
    xmin_coord = Column(Float)
    ymin = Column(Float)
    xmax_coord = Column(Float)
    ymax = Column(Float)
    image_path = Column(String(255))
    detection_time = Column(DateTime, default=datetime.utcnow)
