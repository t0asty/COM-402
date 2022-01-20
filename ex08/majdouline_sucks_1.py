import pandas as pd
from collections import Counter
com402 = pd.read_csv('./anon_data/com402-1.csv', names=['email', 'movie', 'date', 'rating'])
imdb = pd.read_csv('./anon_data/imdb-1.csv', names=['email', 'movie', 'date', 'rating'])

dates = imdb[imdb['email'] == 'donald.trump@whitehouse.gov']['date'].to_list()
trump_id = com402[com402['date'].isin(dates)].groupby('email')['movie'].count().sort_values().index[-1]

hashes = com402[com402['email'] == trump_id]['movie'].to_list()
res = list()

for has in hashes:
    movie = None
    df_dict = com402[com402['movie'] == has][['date', 'rating']].to_dict()
    for key, date in df_dict['date'].items():
        rate = df_dict['rating'][key]
        if movie is None:
            movie = imdb[(imdb['date'] == date)&(imdb['rating'] == rate)]['movie'].to_list()
        else:
            movie += imdb[(imdb['date'] == date)&(imdb['rating'] == rate)]['movie'].to_list()
    c = Counter(movie)
    res.append(c.most_common(1)[0][0])
print(res)