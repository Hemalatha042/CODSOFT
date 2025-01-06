import pandas as pd
import numpy as npe
data = {
    'Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Genre': ['Fiction', 'Drama', 'Dystopian', 'Romance', 'Fiction']
}

df = pd.DataFrame(data)

def cosine_similarity(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    words1, words2 = set(str1.split()), set(str2.split())
    
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    return intersection / union if union != 0 else 0

def recommend_books(user_input, df):
    print(f"Your input genre: {user_input}")
    
    sim_scores = []
    for idx, genre in df['Genre'].items():
        score = cosine_similarity(user_input, genre)
        sim_scores.append((idx, score))
    
    sim_scores.sort(key=lambda x: x[1], reverse=True)
    
    recommended_indices = [score[0] for score in sim_scores if df['Genre'][score[0]] != user_input]
    
    print("\nBooks recommended for you:")
    for idx in recommended_indices[:3]:
        print(f"- {df['Title'][idx]}")

user_input = input("Enter your preferred genre (e.g., 'Fiction', 'Romance'): ")
recommend_books(user_input, df)