from fastapi import FastAPI
from database.db import Base, engine
from controllers.atleta_controller import router as atleta_router
from fastapi_pagination import add_pagination

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="WorkoutAPI - Crossfit",
    description="API criada para o desafio da DIO (FastAPI + Docker + Postgres)",
    version="1.0.0"
)

# Rotas
app.include_router(atleta_router, prefix="/atletas", tags=["Atletas"])

# Paginação
add_pagination(app)


@app.get("/")
def root():
    return {"message": "WorkoutAPI está no ar!"}
