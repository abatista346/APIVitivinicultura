from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/importacao", tags=["Importação"])

@router.get("/")
def listar_importacao():
    dados = {
        "Ano": [2019, 2020, 2021],
        "Volume Importado (t)": [500, 600, 550]
    }
    df = pd.DataFrame(dados)
    return df.to_dict(orient="records")
