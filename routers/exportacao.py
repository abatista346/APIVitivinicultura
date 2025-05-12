from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/exportacao", tags=["Exportação"])

@router.get("/")
def listar_exportacao():
    dados = {
        "Ano": [2019, 2020, 2021],
        "Volume Exportado (t)": [150, 200, 180]
    }
    df = pd.DataFrame(dados)
    return df.to_dict(orient="records")
