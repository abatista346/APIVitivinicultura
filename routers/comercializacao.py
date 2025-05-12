from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/comercializacao", tags=["Comercialização"])

@router.get("/")
def listar_comercializacao():
    dados = {
        "Ano": [2019, 2020, 2021],
        "Volume Comercializado (t)": [3200, 3400, 3600]
    }
    df = pd.DataFrame(dados)
    return df.to_dict(orient="records")
