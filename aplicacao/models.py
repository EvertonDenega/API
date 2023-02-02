from typing import Optional
from pydantic import BaseModel


class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str


alunos = [
    Aluno(id=1, nome="Everton", idade=38, email="e@eu.com"),
    Aluno(id=2, nome="Denega", idade=37, email="d@eu.com"),
    Aluno(id=3, nome="Souza", idade=36, email="s@eu.com")
]
