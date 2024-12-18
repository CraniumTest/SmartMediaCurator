import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ContentRecommender:
    def __init__(self, user_data, content_data):
        self.user_data = user_data
        self.content_data = content_data
        self.similarity_matrix = self._build_similarity_matrix()

    def _build_similarity_matrix(self):
        return cosine_similarity(self.content_data)

    def recommend(self, user_id, top_n=5):
        user_idx = self.user_data.index(user_id)
        user_preferences = self.similarity_matrix[user_idx]
        recommended_indices = np.argsort(-user_preferences)[:top_n]
        return [self.content_data[i] for i in recommended_indices]

# Sample Usage
user_data = ['User1', 'User2', 'User3']
content_data = np.array([[1, 0, 3], [3, 2, 1], [0, 1, 2]])

recommender = ContentRecommender(user_data, content_data)
print(recommender.recommend('User1'))
