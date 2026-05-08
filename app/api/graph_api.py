from fastapi import APIRouter
from app.graph.graph_builder import build_graph

router = APIRouter()

@router.get("/graph")
def get_graph():

    G = build_graph()

    return {
        "nodes": list(G.nodes()),
        "edges": list(G.edges())
    }