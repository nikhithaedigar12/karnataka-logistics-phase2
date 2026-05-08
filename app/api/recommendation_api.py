from fastapi import APIRouter
from app.services.recommendation_engine import recommend_skills

router = APIRouter()

@router.get("/recommend/{skill}")
def get_recommendations(skill: str):

    return recommend_skills(skill)