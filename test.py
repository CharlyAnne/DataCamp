import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']  
netflix_movies = netflix_df[['title', 'country', 'genre', 'release_year', 'duration']]
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Assigning colors to four genre groups
colors = []
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre == 'Children':
        colors.append('pink')
    elif genre == 'Documentaries':
        colors.append('black')
    elif genre == 'Stand-Up':
        colors.append('orange')
    else:
        #'Other' genre
        colors.append('green') 
        
#initializing figure object
fig = plt.figure()
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
