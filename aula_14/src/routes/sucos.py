from fastapi import APIRouter, HTTPException, status

from src.routes.frutas import get_fruta
from src.schemas.sucos_schema import CriarNovoSuco, SucoResponse, AlterarNomeSuco
from src.repository.sucos_repository import (
    cadastrar_suco, get_all_sucos, atualizar_nome_suco
)
from src.translate.traducoes_frutas import fruta_em_ingles


sucos = APIRouter(prefix="/sucos", tags=["Sucos"])


@sucos.post(
    "/",
    response_model=SucoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar um novo suco "
)
async def criar_suco(suco: CriarNovoSuco):
    nome = suco.nome.strip()
    if not nome:
        raise HTTPException(status_code=422, detail="O nome do suco não pode ser vazio.")

    frutas = [fruta.strip().lower() for fruta in suco.frutas]
    desconhecidas = [fruta for fruta in frutas if fruta_em_ingles(fruta) is False]
    if desconhecidas:
        raise HTTPException(status_code=422, detail=f"Fruta(s) não reconhecida(s): {', '.join(desconhecidas)}")

    total_calorias = 0.0
    total_acucar = 0.0
    for fruta in frutas:
        try:
            dados_fruta = await get_fruta(fruta)
        except HTTPException as erro:
            if erro.status_code == 404:
                raise HTTPException(status_code=422, detail=f"Não encontramos dados da fruta '{fruta}'")
            raise
        total_calorias += dados_fruta["calorias"]
        total_acucar += dados_fruta["açúcar"]

    novo_suco = {
        **suco.model_dump(),
        "nome": nome,
        "frutas": frutas,
        "calorias": round(total_calorias, 2),
        "acucar": round(total_acucar, 2)
    }

    cadastrado = cadastrar_suco(novo_suco)
    if cadastrado is None:
        raise HTTPException(status_code=409, detail="Já existe um suco com esse nome.")
    return cadastrado


@sucos.get(
    "/",
    response_model=list[SucoResponse],
    summary="Listar todos os sucos"
)
def listar_sucos():
    return get_all_sucos()


@sucos.put(
    "/{suco_id}",
    response_model=SucoResponse,
    summary="Alterar o nome de um suco pelo ID"
)
def modificar_nome_suco(suco_id: int, dados: AlterarNomeSuco):
    resultado = atualizar_nome_suco(suco_id, dados.nome)

    if resultado == "nao_encontrado":
        raise HTTPException(status_code=404, detail="Suco não encontrado.")
    if resultado == "nome_duplicado":
        raise HTTPException(status_code=409, detail="Já existe outro suco com esse nome.")

    return next(suco for suco in get_all_sucos() if suco["id"] == suco_id)
