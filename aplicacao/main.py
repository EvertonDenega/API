<<<<<<< HEAD
from fastapi import FastAPI 
from fastapi import HTTPException, status
=======
from fastapi import FastAPI, HTTPException, Path, Response, status
from fastapi import Query
from fastapi import Header
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3
from models import Aluno
from fastapi import Response
from fastapi import Path

app = FastAPI()

@app.get('/')
async def raiz():
<<<<<<< HEAD
    return { "mensagem": "Seja bem vindo ao more devs" }
=======
    return {"mensagem": "Seja bem vindo ao more devs"}
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3

alunos = {
    1: {
        "nome": "Everton",
        "idade": "38",
<<<<<<< HEAD
        "email": "e@eu.com"
    },
    2: {
        "nome": "Teste",
        "idade": "17",
        "email": "test@eu.com"
=======
        "email": "eu@eu.com"
    },
    2: {
        "nome": "Prof",
        "idade": "25",
        "email": "andre@zuplae.com"
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3
    }
}

@app.get('/alunos')
async def get_alunos(): 
    return alunos
@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int = Path(default=None, title='ID Aluno', description='deve ser entre 1 ou 2', gt=0, lt=3)): 
    try:
        aluno = alunos[aluno_id]
        return aluno

    except KeyError:
        raise HTTPException(
<<<<<<< HEAD
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado'
=======
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado'
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3
        )

@app.post('/alunos', status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno: Aluno):
<<<<<<< HEAD
    next_id : int = len(alunos) +1
=======
    next_id : int = len(alunos) + 1
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.get('/calculadora') 
async def calcular(a: int,
                   b: int,
                   c: int):

    soma: int = a + b + c
    return {"mensagem": f'O resultado da soma é: {soma}'}


@app.put('/alunos/{aluno_id}')
async def put_aluno(aluno_id: int, aluno: Aluno):
    
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')


@app.delete('/alunos/{aluno_id}')
async def delete_aluno(aluno_id: int):
    
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')




@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), 
                   b: int = Query(default=None, gt=10), 
                   x_geek: str = Header(default=None), 
                   c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c

    print(f'X-GEEK: {x_geek}')
    return {"resultado": soma}

@app.put('/alunos/{aluno_id}')
async def put_aluno(aluno_id: int, aluno: Aluno):
    
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')


@app.delete('/alunos/{aluno_id}')
async def delete_aluno(aluno_id: int):
    
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')




if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
<<<<<<< HEAD
        log_level = "info",
        reload = True
=======
        log_level="info",
        reload=True
>>>>>>> 7e2fbd6034f5b79decde4782c182e2d9de21b9e3
    )