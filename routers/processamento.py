from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/processamento", tags=["Processamento"])

@router.get("/")
def listar_processamento():
    dados = {
        "Ano": [2019, 2020, 2021],
        "Processamento (t)": [3500, 3700, 3900]
    }
    df = pd.DataFrame(dados)
    return df.to_dict(orient="records")
