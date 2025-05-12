from fastapi import FastAPI
from app.routers import producao, processamento, comercializacao, importacao, exportacao

app = FastAPI(
    title="API Vitivinicultura Embrapa",
    description="Consulta aos dados públicos da Embrapa",
    version="1.0.0"
)

# Incluindo os routers
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API da Embrapa Vitivinicultura"}
