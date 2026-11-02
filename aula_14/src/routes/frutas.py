from fastapi import APIRouter, HTTPException
import httpx
from GC_IA_DADOS_2026.aula_14.src.translate.traducoes_frutas import fruta_em_ingles, traduzir_fruta

frutas_router = APIRouter(
    prefix="/frutas",
    tags=["Frutas"]
)

api_fruityvice_url = "https://www.fruityvice.com/api"


@frutas_router.get("/{nome_fruta}")
async def get_fruta(nome_fruta: str):
    url = f"{api_fruityvice_url}/fruit/{fruta_em_ingles(nome_fruta)}"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)

            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail="Fruta não encontrada"
                )    
                    
            response.raise_for_status() 
            resposta = response.json()
        
            resposta = {
                "nome": traduzir_fruta(resposta["name"]),
                "calorias": resposta["nutritions"]["calories"],
                "açúcar": resposta["nutritions"]["sugar"]
            }
            
            return resposta

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="A API externa demorou para responder"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Erro de comunicação com a API externa"
        )

    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=502,
            detail="Erro retornado pela API externa"
        )
