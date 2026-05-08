from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.services.data_loader import load_data

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_skills(target_skill):

    df = load_data()

    skills = df["skill"].tolist()

    embeddings = model.encode(skills)

    target_embedding = model.encode([target_skill])

    similarity_scores = cosine_similarity(
        target_embedding,
        embeddings
    )[0]

    recommendations = []

    for skill, score in zip(skills, similarity_scores):

        recommendations.append({
            "skill": skill,
            "similarity_score": float(score)
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["similarity_score"],
        reverse=True
    )

    return recommendations[:5]