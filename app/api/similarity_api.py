from fastapi import APIRouter
from app.services.similarity_engine import find_similar_skills

router = APIRouter()

@router.get("/similarity")
def get_similarity():

    return find_similar_skills()