from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.services.data_loader import load_data

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_similar_skills():

    df = load_data()

    skills = df["skill"].tolist()

    embeddings = model.encode(skills)

    similarity_matrix = cosine_similarity(embeddings)

    results = []

    for i in range(len(skills)):

        results.append({
            "skill": skills[i],
            "similarity_scores": similarity_matrix[i].tolist()
        })

    return results