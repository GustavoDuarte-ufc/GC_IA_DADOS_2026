"""
Testes do endpoint POST /sucos/

Rode na raiz do projeto com:
    pip install pytest
    pytest src/tests/test_cadastrar_suco.py
"""
import pytest
from fastapi.testclient import TestClient

import GC_IA_DADOS_2026.aula_14.src.db.conn as conn_module
import GC_IA_DADOS_2026.aula_14.src.routes.sucos as sucos_module
from GC_IA_DADOS_2026.aula_14.main import app

# Valores falsos para não depender da internet durante o teste
FRUTAS_FALSAS = {
    "banana": {"nome": "banana", "calorias": 96, "açúcar": 17.2},
    "manga": {"nome": "manga", "calorias": 60, "açúcar": 13.7},
}


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Usa um banco temporário, para não sujar o banco de verdade
    monkeypatch.setattr(conn_module, "DB_PATH", tmp_path / "teste.db")

    async def get_fruta_falsa(nome):
        return FRUTAS_FALSAS[nome]

    monkeypatch.setattr(sucos_module, "get_fruta", get_fruta_falsa)

    with TestClient(app) as c:
        yield c


def test_cadastra_suco_somando_calorias_e_acucar(client):
    resposta = client.post("/sucos/", json={
        "nome": "Tropical",
        "frutas": ["Banana", "manga"],
        "descricao": "Banana com manga",
    })

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["id"] == 1
    assert corpo["frutas"] == ["banana", "manga"]
    assert corpo["calorias"] == 156
    assert corpo["acucar"] == 30.9


def test_recusa_fruta_desconhecida(client):
    resposta = client.post("/sucos/", json={
        "nome": "Estranho",
        "frutas": ["banana", "pedra"],
        "descricao": "Não existe",
    })

    assert resposta.status_code == 422
    assert "pedra" in resposta.json()["detail"]


def test_recusa_suco_sem_frutas(client):
    resposta = client.post("/sucos/", json={
        "nome": "Vazio",
        "frutas": [],
        "descricao": "Sem nada",
    })

    assert resposta.status_code == 422


def test_recusa_nome_muito_longo(client):
    resposta = client.post("/sucos/", json={
        "nome": "N" * 21,
        "frutas": ["banana"],
        "descricao": "Nome grande",
    })

    assert resposta.status_code == 422
