from sqlalchemy.orm import Session
import models, schemas

def get_detection(db: Session, detection_id: int):
    return db.query(models.Detection).filter(models.Detection.id == detection_id).first()

def get_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Detection).offset(skip).limit(limit).all()

def create_detection(db: Session, detection: schemas.DetectionCreate):
    db_detection = models.Detection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
# Update detection by ID
def update_detection(db: Session, detection_id: int, detection_update: schemas.DetectionUpdate):
    db_detection = db.query(models.Detection).filter(models.Detection.id == detection_id).first()
    
    if not db_detection:
        return None
    
    # Update the fields
    for key, value in detection_update.dict(exclude_unset=True).items():
        setattr(db_detection, key, value)
    
    db.commit()
    db.refresh(db_detection)
    
    return db_detection

