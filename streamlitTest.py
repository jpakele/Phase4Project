import streamlit as st
st.write('litteraly anything else more')

def anything(n):
    return st.write(5 + n)

anything(5)

import pandas as pd
import numpy as np
movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')

ratings = ratings.drop(columns = 'timestamp')
ratings.head()

from surprise.prediction_algorithms import SVD
svd = SVD()

def recommended_movies(user_ratings,movie_title_df,n):
        for idx, rec in enumerate(user_ratings):
            title = movie_title_df.loc[movie_title_df['movieId'] == int(rec[0])]['title']
            print('Recommendation # ', idx+1, ': ', title, '\n')
            n -= 1
            if n == 0:
                break


movie_df = movies
num_of_rated_movies = 4
genre = 'Comedy'

userID = 1000
rating_list = []
print(f'Thank you for participating! In order to obtain your recommendations, please rate {num_of_rated_movies} movies.')

# This portion grabs a random movie title and info and asks the user to rate it
# Once the user gives a number 1-5 or n (for haven't seen), it will append it
# To the rating_list.


def give_example(num, kee, genre=None):
    st.write('On a scale of 1 - 5, how would you rate this movie? press n if you have not seen this movie. Press enter to submit your answer: \n')
    options = ['...', 1, 2, 3, 4, 5, 'n']
    while len(rating_list) != num:
        if genre:
            movie = movie_df[movie_df['genres'].str.contains(genre)].sample(1)
        else:
            movie = movie_df.sample(1)
        st.write(movie)
        rating = st.selectbox('select one, please', options, key = kee)
        kee += 1
        if rating == 'n':
                break
        if rating == '...':
                break
        if rating in (1, 2, 3, 4, 5):
            rating_one_movie = {'userId':userID, 'movieId':movie['movieId'].values[0], 'rating':rating}
            rating_list.append(rating_one_movie)


def run_and_rerun(num, genre=None):
    st.write(rating_list)
    kee = 0
    if len(rating_list) == 0:
        st.write(give_example(num, kee,  genre=None))
        num -= 1
    if len(rating_list) == 1:
        st.write(give_example(num, kee, genre=None))
        num -= 1
    if len(rating_list) == 2:
        st.write(give_example(num, kee, genre=None))
        num -= 1
    if len(rating_list) == 3:
        st.write(give_example(num, kee, genre=None))
        num -= 1
    if len(rating_list) == 4:
        from surprise.similarities import cosine, msd, pearson
        from surprise import accuracy
        from surprise import Reader, Dataset
        from surprise.model_selection import train_test_split

        #loading the .CSV file into surprise
        reader = Reader()
        data = Dataset.load_from_df(ratings,reader)
        train, test = train_test_split(data, test_size=0.2)
        
        new_rating_df = ratings.append(rating_list, ignore_index = True)
        new_data = Dataset.load_from_df(new_rating_df, reader)
        svd = SVD(n_factors=100, n_epochs=10, lr_all=0.005, reg_all=0.4)
        svd.fit(new_data.build_full_trainset())
        predictions = svd.test(test)
        
        moviesList = []
        for m_id in ratings['movieId'].unique():
            moviesList.append((m_id, svd.predict(1000, m_id)[3]))
        
        # This portion takes the list of predictions and orders them in order
        # of most likely to be liked by the user to least.
        ranked_movies = sorted(moviesList, key=lambda x:x[1], reverse=True)
        
        # This takes in the list of predicted movies, the DataFrame of movies,
        # and a number reguarding how many movies to show (starting from the top)
    st.text(recommended_movies(ranked_movies,movies,5))
    

st.write(run_and_rerun(4, 'Comedy'))

st.write(rating_list)
