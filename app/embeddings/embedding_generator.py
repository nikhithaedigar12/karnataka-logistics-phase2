from sentence_transformers import SentenceTransformer
from app.services.data_loader import load_data

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings():

    df = load_data()

    skills = df["skill"].tolist()

    embeddings = model.encode(skills)

    result = []

    for skill, vector in zip(skills, embeddings):

        result.append({
            "skill": skill,
            "embedding_dimension": len(vector),
            "sample_values": vector[:5].tolist()
        })

    return result