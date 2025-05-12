from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/producao", tags=["Produção"])

@router.get("/")
def listar_producao():
    # Simulando dados
    dados = {"Ano": [2019, 2020, 2021], "Produção (t)": [4000, 4200, 4500]}
    df = pd.DataFrame(dados)
    return df.to_dict(orient="records")
