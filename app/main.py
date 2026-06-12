from fastapi import FastAPI

app = FastAPI(
    title="Projeto Integrador API",
    description="API desenvolvida com FastAPI.",
    version="0.1.0",
)


@app.get("/", tags=["Geral"])
async def root() -> dict[str, str]:
    return {"message": "API funcionando!"}


@app.get("/users")
def list_users():
    db: Session = SessionLocal()

    users = db.query(User).all()

    return users


@app.post("/users")
def create_user(nome: str, numero: str = ""):
    db: Session = SessionLocal()

    user = User(name=nome, numero=numero)

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "id": user.id,
        "name": user.name,
        "numero": user.numero
    }