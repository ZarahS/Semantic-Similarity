# Program that will tell you what to watch next based on the word vector similarity of movie descriptions.

# Import spacy module
import spacy

# Function that takes in movie description as parameter and returns the most similar movie 
def next_movie(description):

    # load the english language model
    nlp = spacy.load('en_core_web_md')

    # process description of previously watched movie
    doc = nlp(description)
    
    # open movies.txt file for reading 
    with open("movies.txt", "r") as f:

        # Initialize an empty list to store the processed movie descriptions
        movies = []

        # process each movie in txt file and add to movies list
        for line in f.readlines():
            movie = nlp(line[9:])
            movies.append(movie)

        # Find the movie with the highest similarity score to the previously watched movie
        best_match = max(movies, key=lambda x: x.similarity(doc))

    # Create a dictionary mapping movie descriptions to movie letters
    movie_dict = {movies[i].text: chr(i + ord('A')) for i in range(len(movies))}
    
    # Return the movie with the highest similarity score
    return f"Your next movie is '{movie_dict[best_match.text]}' with a similarity of {best_match.similarity(doc):.2f}"

# Previously watched movie description
prev_watch = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,\
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.\
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call on next movie function and print recommendation
print(next_movie(prev_watch))




