import json
import sqlite3
from src.db.conn import conexao


def cadastrar_suco(suco: dict):
    conn = conexao()
    try:
        cursor = conn.cursor()
        # A comparação sem distinção entre maiúsculas/minúsculas evita nomes duplicados.
        cursor.execute("SELECT id FROM sucos WHERE nome = ? COLLATE NOCASE", (suco["nome"].strip(),))
        if cursor.fetchone():
            return None

        cursor.execute(
            """INSERT INTO sucos (nome, frutas, descricao, calorias, acucar)
               VALUES (?, ?, ?, ?, ?)""",
            (suco["nome"].strip(), json.dumps(suco["frutas"], ensure_ascii=False),
             suco["descricao"], suco["calorias"], suco["acucar"])
        )
        conn.commit()
        return {"id": cursor.lastrowid, **suco, "nome": suco["nome"].strip()}
    except sqlite3.IntegrityError:
        conn.rollback()
        return None
    finally:
        conn.close()


def get_all_sucos():
    conn = conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, frutas, descricao, calorias, acucar FROM sucos ORDER BY id")
        rows = cursor.fetchall()
        return [
            {"id": row[0], "nome": row[1], "frutas": json.loads(row[2]),
             "descricao": row[3], "calorias": row[4], "acucar": row[5]}
            for row in rows
        ]
    finally:
        conn.close()


def atualizar_nome_suco(suco_id: int, novo_nome: str):
    conn = conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM sucos WHERE id = ?", (suco_id,))
        if cursor.fetchone() is None:
            return "nao_encontrado"

        cursor.execute(
            "SELECT id FROM sucos WHERE nome = ? COLLATE NOCASE AND id != ?",
            (novo_nome.strip(), suco_id)
        )
        if cursor.fetchone():
            return "nome_duplicado"

        cursor.execute("UPDATE sucos SET nome = ? WHERE id = ?", (novo_nome.strip(), suco_id))
        conn.commit()
        return "atualizado"
    except sqlite3.IntegrityError:
        conn.rollback()
        return "nome_duplicado"
    finally:
        conn.close()
