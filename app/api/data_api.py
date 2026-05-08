from fastapi import APIRouter
from app.services.data_loader import load_data

router = APIRouter()

@router.get("/workers")
def get_workers():
    df = load_data()
    return df.to_dict(orient="records")
    