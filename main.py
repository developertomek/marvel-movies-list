import pandas as pd

link = "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films"
movies_table = pd.read_html(link)
infinity_saga_data = movies_table[1]
multiverse_saga_data = movies_table[2]


def get_movies(data):
    movies = []
    for _, row in data.iterrows():
        movie_dict = {
            "title": row.iloc()[0],
            "release_date": row.iloc()[1],
            "director": row.iloc()[2],
            "screenwriter": row.iloc()[3],
            "producer": row.iloc()[4]
        }
        movies.append(movie_dict)
    return movies


infinity_saga = get_movies(infinity_saga_data)
multiverse_saga = get_movies(multiverse_saga_data)

all_movies = infinity_saga + multiverse_saga
print(all_movies)
