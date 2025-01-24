from sqlalchemy.orm import Session
import crud
import models
import schemas
import dependencies
from typing import Optional
from datetime import datetime
import numpy as np

def create_elements(payload: dict, db: Session):
    elements = []
    for key, value in payload.items():
        element_data = schemas.ElementCreate(**value)
        flat_data, normalized_data = element_data.normalize_data()

        avg_before = np.mean(flat_data)
        avg_after = np.mean(normalized_data)
        data_size = len(flat_data)

        device = db.query(models.Device).filter_by(device_name=element_data.device_name).first()
        if not device:
            device = models.Device(device_name=element_data.device_name)
            db.add(device)
            db.commit()
            db.refresh(device)

        element = models.Element(
            device_id=device.id,
            average_before_normalization=avg_before,
            average_after_normalization=avg_after,
            data_size=data_size
        )
        db.add(element)
        db.commit()
        db.refresh(element)
        elements.append(element)

    return elements

def get_elements(created_date: Optional[datetime], db: Session):
    query = db.query(models.Element).join(models.Device)
    if created_date:
        query = query.filter(models.Element.created_date == created_date)
    return query.all()

def get_element_by_id(id: int, db: Session):
    return db.query(models.Element).filter(models.Element.id == id).first()

def update_element(id: int, device_name: Optional[str], db: Session):
    element = db.query(models.Element).filter(models.Element.id == id).first()
    if device_name:
        device = db.query(models.Device).filter_by(device_name=device_name).first()
        if not device:
            device = models.Device(device_name=device_name)
            db.add(device)
            db.commit()
            db.refresh(device)
        element.device_id = device.id
    db.commit()
    db.refresh(element)
    return element

def delete_element(id: int, db: Session):
    element = db.query(models.Element).filter(models.Element.id == id).first()
    db.delete(element)
    db.commit()
