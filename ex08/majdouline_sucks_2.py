import pandas as pd
from collections import Counter
com402 = pd.read_csv('./anon_data/com402-2.csv', names=['email', 'movie', 'date', 'rating'])
imdb = pd.read_csv('./anon_data/imdb-2.csv', names=['email', 'movie', 'date', 'rating'])

hashes = com402['movie'].value_counts().index
movies = imdb['movie'].value_counts().index

hash_to_movie = {hashes[i]: movies[i] for i in range(len(movies))}
movie_to_hash = {movies[i]: hashes[i] for i in range(len(movies))}

trump_movies = [movie_to_hash[mov] for mov in imdb[imdb['email'] == 'donald.trump@whitehouse.gov']['movie'].to_list()]
trump_hash = com402[com402['movie'].isin(trump_movies)]['email'].value_counts().index[0]

print([hash_to_movie[has] for has in com402[com402['email'] == trump_hash]['movie'].to_list()])
#print(imdb.head())