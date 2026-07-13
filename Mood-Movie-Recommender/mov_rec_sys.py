def recommend_movie(mood):
  recommendations = {
    "happy": ["Leagally Blonde, Clueless, Crazy Rich Asians, "],
    "funny": ["Barbie, Don't Look Up, The French Budapest, Jumanji, The Spy Next Door"],
    "romantic": ["La La Land, Pride and Prejudice, Eternal Sunshine, Challegers, Past Lives"],
    "sad": ["The Notebook, Titanic, Schlinder's List, Forrest Grump, Marriage Story"],
    "angry": ["Falling Down, I Stand Alone, The Accused, Fight Club, John Wick"],
    "excited": ["13 going on 30, Back to the Future, Bridesmaid, Inception"],
    "bored": ["Pulp Fiction, The Dark Knight, Zombieland, The Grand Budapest Hotel"],
    "scared": ["Hereditary, Scream, Get Out, The Conjuring, Hocus Pocus"],
    "stressed": ["3 idiots, A Beautiful Mind, Inside Out, The Black Swan, Whiplash"],
    "relaxed": ["Finding Nemo, Toy Story, Spirited Away, Despicable Me, Kung Fu Panda"],
    "nostalgic": ["The Breakfast Club, Jab We Met, Stand By Me"]
  }

  mood = mood.lower()
  if mood in recommendations:
    return f"Based on your mood ({mood}), we recommend: {recommendations[mood][0]}."
  else:
    return "Sorry, I don't have recommendations for that mood."

user_mood = input("How are you feeling today? (happy, funny, romantic, sad, angry, excited, bored, scared, stressed, relaxed, nostalgic): ")
print(recommend_movie(user_mood))
