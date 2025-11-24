from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from services.atleta_service import AtletaService
from schemas.atleta import (
    AtletaCreate,
    AtletaResponse,
    AtletaResponseDetail
)
from fastapi_pagination import Page, paginate

router = APIRouter()
service = AtletaService()


@router.get("/", response_model=Page[AtletaResponse])
def listar_atletas(
    nome: str | None = None,
    cpf: str | None = None,
    db: Session = Depends(get_db),
):
    atletas = service.listar_atletas(db, nome=nome, cpf=cpf)
    return paginate(atletas)


@router.get("/{atleta_id}", response_model=AtletaResponseDetail)
def obter(atleta_id: int, db: Session = Depends(get_db)):
    return service.obter_atleta(db, atleta_id)


@router.post("/", response_model=AtletaResponseDetail)
def criar(atleta: AtletaCreate, db: Session = Depends(get_db)):
    return service.criar_atleta(db, atleta)


@router.delete("/{atleta_id}")
def deletar(atleta_id: int, db: Session = Depends(get_db)):
    return service.remover_atleta(db, atleta_id)
