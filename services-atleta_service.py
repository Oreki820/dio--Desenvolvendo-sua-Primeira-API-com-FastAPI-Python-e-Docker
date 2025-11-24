from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.atleta import Atleta
from schemas.atleta import AtletaCreate


class AtletaService:

    def listar_atletas(self, db: Session, nome: str = None, cpf: str = None):
        query = db.query(Atleta)

        if nome:
            query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
        if cpf:
            query = query.filter(Atleta.cpf == cpf)

        return query.all()

    def obter_atleta(self, db: Session, atleta_id: int):
        atleta = db.query(Atleta).filter(Atleta.id == atleta_id).first()
        if not atleta:
            raise HTTPException(status_code=404, detail="Atleta não encontrado")
        return atleta

    def criar_atleta(self, db: Session, atleta: AtletaCreate):
        novo_atleta = Atleta(**atleta.dict())

        try:
            db.add(novo_atleta)
            db.commit()
            db.refresh(novo_atleta)
            return novo_atleta

        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=303,
                detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
            )

    def remover_atleta(self, db: Session, atleta_id: int):
        atleta = self.obter_atleta(db, atleta_id)
        db.delete(atleta)
        db.commit()
        return {"message": "Atleta removido com sucesso"}
