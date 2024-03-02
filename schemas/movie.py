from typing import Optional
from pydantic import BaseModel, Field


# ESQUEMA PYDANTIC BaseModel, None es valor por default. Con Field coloco validaciones y valores por defecto
#le: menor que 2024
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    model_config = {
        "json_schema_extra": {
            "examples": [{
                'title': 'Mi Película',
                'overview': 'Descripción de la película',
                'year': 2024,
                'rating': 10.0,
                'category': 'Accion'
            }]
        }
    }