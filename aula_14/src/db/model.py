from src.db.conn import conexao


def criar_tabelas():
    conn = conexao()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sucos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                frutas TEXT NOT NULL,
                descricao TEXT NOT NULL,
                calorias REAL NOT NULL CHECK (calorias >= 0),
                acucar REAL NOT NULL CHECK (acucar >= 0)
            )
        """)

        conn.commit()

    finally:
        conn.close()
