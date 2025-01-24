from pydantic import BaseModel,  field_validator
from typing import List
from datetime import datetime

class ElementCreate(BaseModel):
    id: str
    data: List[str]
    device_name: str

    @field_validator("data", mode="before")
    def validate_data(cls, v):
        # Verificar que todos los elementos en la lista de datos sean números
        if not all(item.isdigit() for item in v.split()):
            raise ValueError("All data elements must be numbers.")
        return v

    def normalize_data(self):
        flat_data = [int(num) for line in self.data for num in line.split()]
        max_val = max(flat_data)
        normalized = [x / max_val for x in flat_data]
        return flat_data, normalized

class ElementResponse(BaseModel):
    id: int
    device_name: str
    average_before_normalization: float
    average_after_normalization: float
    data_size: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True  