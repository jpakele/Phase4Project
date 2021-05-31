# Business Goal
The goal of this project is to create a useable program the takes in user input and gives movie recommendations base on the user's interaction.

## The Data
The data for this project was based on the MovieLens dataset from the GroupLens research lab at the University of Minnesota. It is the smaller of two dataset as this program was meant to run locally. Three DataFrames: 'movies', 'ratings', and 'tags'. The dataset it self consists of 100,00 records of movies, users and ratings, genres, and descriptive tags for each movie.

## Cleaning the Data
The data in this Dataset was extremely clean and did not require much modifying.

In the DataFrame "ratings" only one column needed to be dropped in order to make the data readable. The column 'timestamp' was dropped as it was extraneous in the first place

For this program, on the 'movies' and 'ratings' DataFrames were used.

## Model Testing
10 model's were run and tested for accuracy and time efficiency.
- KNNBasic
- KNNWithMeans
- KNNWithZScore
- KNNBaseline
- SVD
- NormalPredictor
- BaselineOnly
- NMF
- SlopeOne
- CoClustering

SVD was selected for being both sufficiently quick and accurate as well as having a more detailed documentation of parameters.

Parameters were found with by running a grid search and then fitted onto the dataset base on other users and their ratings.

## Results
The program is set to give the user a random movie from the dataset, ask them for a rating of 1-5 or to skip. The program is set to require 4 ratings to get a prediction, though this number can be modified. The program will then give the top 5 most likely to be interesting to the user, though this number can also be changed.

The program itself has an average RMSE score of about .8