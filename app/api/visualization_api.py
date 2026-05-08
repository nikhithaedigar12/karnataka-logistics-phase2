from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.graph.graph_visualizer import visualize_graph

router = APIRouter()

@router.get("/visualize")
def visualize():

    image_path = visualize_graph()

    return FileResponse(image_path)