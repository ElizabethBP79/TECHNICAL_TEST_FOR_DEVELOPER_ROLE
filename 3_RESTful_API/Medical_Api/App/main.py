from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
import dependencies
from typing import Optional
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/api/elements/", response_model=list[schemas.ElementResponse])
def create_elements(payload: dict, db: Session = Depends(dependencies.get_db)):
    elements = crud.create_elements(payload, db)
    return elements

@app.get("/api/elements/", response_model=list[schemas.ElementResponse])
def list_elements(
    created_date: Optional[datetime] = None, db: Session = Depends(dependencies.get_db)
):
    elements = crud.get_elements(created_date, db)
    return elements

@app.get("/api/elements/{id}/", response_model=schemas.ElementResponse)
def get_element(id: int, db: Session = Depends(dependencies.get_db)):
    element = crud.get_element_by_id(id, db)
    return element

@app.put("/api/elements/{id}/", response_model=schemas.ElementResponse)
def update_element(id: int, device_name: Optional[str] = None, db: Session = Depends(dependencies.get_db)):
    element = crud.update_element(id, device_name, db)
    return element

@app.delete("/api/elements/{id}/", response_model=dict)
def delete_element(id: int, db: Session = Depends(dependencies.get_db)):
    crud.delete_element(id, db)
    return {"message": "Element deleted successfully"}