from pydantic import BaseModel, Field

class SucoBase(BaseModel):
    nome: str = Field(min_length=2, max_length=20)
    frutas: list[str] = Field(min_length=1)
    descricao: str = Field(min_length=1, max_length=40)
    calorias: float = Field(ge=0)
    acucar: float = Field(ge=0)
    
class CriarNovoSuco(BaseModel):
    # Mesmas regras do SucoBase. Calorias e açúcar NÃO vêm do cliente:
    # são calculados a partir das frutas.
    nome: str = Field(min_length=2, max_length=20, examples=["Tropical"])
    frutas: list[str] = Field(min_length=1, examples=[["banana", "manga"]])
    descricao: str = Field(min_length=1, max_length=40, examples=["Banana com manga"])
    
class SucoResponse(CriarNovoSuco):
    id: int
    calorias: float
    acucar: float
    
class ModificarSuco(BaseModel):
    nome: str | None = Field(default=None, min_length=2, max_length=20)
    frutas: list[str] | None = Field(default=None, min_length=1)
    descricao: str | None = Field(default=None, min_length=1, max_length=40)
    calorias: float | None = Field(default=None, ge=0)
    acucar: float | None = Field(default=None, ge=0)


class AlterarNomeSuco(BaseModel):
    nome: str = Field(min_length=2, max_length=20)
