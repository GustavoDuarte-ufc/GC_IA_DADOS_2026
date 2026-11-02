import sqlite3
from pathlib import Path

# Caminho fixo do banco (na raiz do projeto), não importa de onde a API for iniciada
DB_PATH = Path(__file__).resolve().parents[2] / "casa_de_sucos.db"


def conexao() -> sqlite3.Connection:
    # Retorna a CONEXÃO (e não o cursor), pois quem chama precisa de
    # conn.cursor(), conn.commit() e conn.close()
    return sqlite3.connect(DB_PATH)
