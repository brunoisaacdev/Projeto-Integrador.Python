from fastapi import FastAPI

app = FastAPI(
    title="Projeto Integrador API",
    description="API desenvolvida com FastAPI.",
    version="0.1.0",
)


@app.get("/", tags=["Geral"])
async def root() -> dict[str, str]:
    return {"message": "API funcionando!"}


@app.get("/health", tags=["Geral"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
