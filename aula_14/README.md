# API Casa de Sucos

Desenvolvido uma API que faz cadastro de sucos e salva em um banco de dados do SQLite. <br>O sistema consome informações de frutas da API pública Fruityvice e retorna calorias e açúcar.

## Tags

### Frutas
GET/ frutas /{nome_fruta} <br> Retorna json com nome, caloria e açúcar.
> {
  "nome": "maçã",
  "calorias": 52,
  "açúcar": 10.3
}

### Sucos
GET / sucos / <br> Listar todos os sucos
>{
    "nome": "Tropical",
    "frutas": [
      "banana",
      "manga"
    ],
    "descricao": "Banana com manga",
    "id": 0,
    "calorias": 0,
    "acucar": 0
  }

POST / sucos / <br> Cadastrar um novo suco
>{
  "nome": "Tropical",
  "frutas": [
    "banana",
    "manga"
  ],
  "descricao": "Banana com manga"
}

PUT / sucos / {suco_id} <br> Modifica o nome do suco do suco_id
>{
  "nome": "string"
}

##  Instruções de Execução

Ambiente Virtual
> python -m venv venv
> .\venv\Scripts\Activate.ps1

Bibliotecas
> pip install -r requirements.txt

Rodar
> uvicorn main:app --reload

Swagger (ambiente local): http://127.0.0.1:8000/docs


