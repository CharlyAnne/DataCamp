# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']  
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Assigning colors to four genre groups
colors = []
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre == 'Children':
        colors.append('blue')
    elif genre == 'Documentaries':
        colors.append('black')
    elif genre == 'Stand-Up':
        colors.append('orange')
    else:
        #'Other' genre
        colors.append('brown') 
        
#initializing figure object
fig = plt.figure()
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

#"Are we certain that movies are getting shorter?"
answer = "no"

