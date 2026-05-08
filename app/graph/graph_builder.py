import networkx as nx
from app.services.data_loader import load_data

def build_graph():
    df = load_data()

    G = nx.Graph()

    for _, row in df.iterrows():

        worker = row["worker_id"]
        job = row["job_id"]
        employer = row["employer_id"]
        skill = row["skill"]

        G.add_node(worker, type="worker")
        G.add_node(job, type="job")
        G.add_node(employer, type="employer")
        G.add_node(skill, type="skill")

        G.add_edge(worker, job)
        G.add_edge(worker, employer)
        G.add_edge(worker, skill)

    return G