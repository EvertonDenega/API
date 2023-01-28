from typing import List
from fastapi import FastAPI 
from fastapi import HTTPException, status
from pydantic import BaseModel
from models import Alunos


app = FastAPI()

@app.get('/')
async def raiz():
    return { "mensagem": "BEM VINDO" }

alunos = {
    1: "Everton",
    2: "Vander",
    3: "João",
    4: "Thiago"
}

alunos = [
    {"id": 1, "name": "William" }
]

class Aluno(BaseModel):
    id: int
    name: str


@app.get('/alunos')
async def get_alunos(): 
    return alunos

@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int) -> List[Aluno]:
    try:
        aluno = alunos[aluno_id]
        alunos.update({
            'id': aluno_id
            })
        
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado')
       
    return aluno


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload = True
    )


professores = {
    1: {'nome': 'Everton', 'idade': 37, 'e-mail': 'e@localhost'},
    2: {"nome": "Andre", "idade": 23, "e-mail": "a@localhost"},
    3: {"nome": "William", "idade": 28, "e-mail": "w@localhost"}
}


@app.get('/professores')
async def get_professores(): 
    return professores

@app.get('/professoresNome/{prof_nome}')
async def get_professor_por_chave(prof_nome: str):
    for professor in professores.values():
        if professor['nome'] == prof_nome:
            return professor
    

@app.post("/aluno/")
async def post_aluno(aluno: Aluno):
    next_id = int(len(aluno))
    aluno = {
        "next_id" : 0,
        "nome" : "Everton",
        "idade" : 38,
        "email" : "evert@gmail.com"
    }

    return aluno