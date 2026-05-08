from fastapi import FastAPI

from app.api.data_api import router as data_router
from app.api.graph_api import router as graph_router
from app.api.embedding_api import router as embedding_router
from app.api.similarity_api import router as similarity_router
from app.api.recommendation_api import router as recommendation_router
from app.api.visualization_api import router as visualization_router

app = FastAPI()

app.include_router(data_router)
app.include_router(graph_router)
app.include_router(embedding_router)
app.include_router(similarity_router)
app.include_router(recommendation_router)
app.include_router(visualization_router)

@app.get("/")
def home():
    return {"message": "Phase 2 Hypergraph Service Running"}