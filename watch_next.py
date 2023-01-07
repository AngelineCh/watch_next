# import spacy and loading md
import spacy
nlp = spacy.load('en_core_web_md')

# adding Hulk movie description
movie_description = '''Will he save their world or destroy it? When the Hulk becomes too
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and
launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery
and trained as a gladiator.'''

# creating nlp var from movie_description
movie_nlp = nlp(movie_description)

# main function, opens movies text file and creates new list to add results
# for each movie in file comparing similarity with Hulk movie description and adds results to list
# finding the index number of the max of the list and splitting the matching indexed movie in title and description
# then printing the title

def movies_recommendation():
    with open ("movies.txt", "r", encoding="utf-8") as movies:
        movies = movies.readlines()
        similarity_list = []
        for token in movies:
            token = nlp(token)
            similarity_list.append((token.similarity(movie_nlp)))

        max_index = similarity_list.index(max(similarity_list))
        title = movies[max_index].split(":")
        print("Movie recommentation based on your preferences:\n{}".format(title[0]))
    

movies_recommendation()
  
