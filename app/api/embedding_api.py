from fastapi import APIRouter
from app.embeddings.embedding_generator import generate_embeddings

router = APIRouter()

@router.get("/embeddings")
def get_embeddings():

    return generate_embeddings()