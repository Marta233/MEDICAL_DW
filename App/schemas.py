from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DetectionCreate(BaseModel):
    img_name: str
    name: str
    confidence: float
    xmin_coord: float
    ymin: float
    xmax_coord: float
    ymax: float
    image_path: str

class Detection(BaseModel):
    id: int
    img_name: str
    name: str
    confidence: float
    xmin_coord: float
    ymin: float
    xmax_coord: float
    ymax: float
    image_path: str
    detection_time: datetime

    class Config:
        from_attributes = True


# Schema for updating a detection
class DetectionUpdate(BaseModel):
    img_name: Optional[str] = None
    name: Optional[str] = None
    confidence: Optional[float] = None
    xmin_coord: Optional[float] = None
    ymin: Optional[float] = None
    xmax_coord: Optional[float] = None
    ymax: Optional[float] = None
    image_path: Optional[str] = None
    detection_time: Optional[datetime] = None

    class Config:
        orm_mode = True

