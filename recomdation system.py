import pandas as pd
data = {
    'Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Genre': ['Fiction', 'Drama', 'Dystopian', 'Romance', 'Fiction']
}
df = pd.DataFrame(data)
def cosine_similarity(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    return 1 if str1 == str2 else 0
def recommend_books(user_input, df):
    print(f"Your preferred genre is: '{user_input}'")
    sim_scores = []
    for idx, row in df.iterrows():
        genre = row['Genre']
        score = cosine_similarity(user_input, genre)
        sim_scores.append((idx, score))
    sim_scores.sort(key=lambda x: x[1], reverse=True)
    recommended_indices = [score[0] for score in sim_scores if df['Genre'][score[0]] != user_input]
    print("\nHere are some books you might like based on your preferred genre:")
    if recommended_indices:
        for idx in recommended_indices[:3]:
            print(f"- {df['Title'][idx]} ({df['Genre'][idx]})")
    else:
        print("Sorry, no recommendations found.")
user_input = input("Enter your preferred genre (e.g., 'Fiction', 'Romance'): ")
recommend_books(user_input, df)
