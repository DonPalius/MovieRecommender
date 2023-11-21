import configparser
import pandas as pd
import sys
import requests
config_obj = configparser.ConfigParser()

''' Creates new csv file combining movieID, title and overview of the movie from movie database using their API '''

''' reading config file '''
config_obj.read("./config.ini")
settings = config_obj["settings"]
user_info = config_obj["user_info"]

def load_data(path: str, sep="::", header=None) -> pd.DataFrame:
    ''' loading dataset with error handling '''
    try:
        df = pd.read_csv(path, sep=sep,
                         header=header, engine="python")

    except FileNotFoundError:
        print(f"File {path} could not be found")
        sys.exit()

    except OSError:
        print(f"File {path} could not be read")
        sys.exit()

    return df


def clear_title(title: str) -> str:
    ''' remove the date at the end of the default title name'''
    return title[:-7]
    
def limit_movies(movies: pd.DataFrame, ratings: pd.DataFrame, threshold=300):
    ''' returns new movie and ratings dataset without movies with less that {threshold} ratings '''
    toDrop = set()
    for movie in set(movies['movieID']):
        if (len(ratings[ratings['movieID'] == movie]) < threshold):
            toDrop.add(movie)

    movies = movies[~movies['movieID'].isin(toDrop)]
    ratings = ratings[~ratings['movieID'].isin(toDrop)]

    return (movies, ratings)

def get_movie_overview(title, api_key) -> str:
    ''' returns movie's plot overview from movie database'''
    print(f"Looking for a oveerview of movie called: {title}")

    # search for movie with given title in movie database
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": title}
    data = requests.get(base_url, params=params).json()

    if len(data['results']) == 0:
        return ""

    # get the plot overview
    overview = data["results"][0]["overview"]
    return overview

if __name__ == '__main__':
    # load dataframes
    # https://www.themoviedb.org/ API key
    API_KEY = user_info["api_key"]

    # load movies dataset
    movies = load_data("./data/movies.dat")
    movies.columns = ['movieID', 'title', 'genre']
    movies = movies.drop(['genre'], axis=1)

    # limit movies number
    ratings = load_data("./data/ratings.dat")
    ratings.columns = ['userID', 'movieID', 'rating', 'timestamp']

    # apply the threshold of using movies with more than threshold ratings
    # to avoid to base the research on too obscure (niche) items
    movies, ratings = limit_movies(
        movies, ratings, int(settings["drop_threshold"]))

    # append overview to each movie
    overviews = {title: get_movie_overview(
        clear_title(title), API_KEY) for title in set(movies['title'])}
    movies['overview'] = movies['title'].map(overviews)

    # save to a file
    movies.to_csv("./data/plots.csv", index=False)
