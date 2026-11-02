from pydantic import BaseModel, Field

class Frutas(BaseModel):
    nome: str = Field(min_length=2, max_length=15)
    calorias: float = Field(ge=0)
    acucar: float = Field(ge=0)