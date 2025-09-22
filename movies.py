import random

age = int(input("Enter age: "))

kids_movies = [
    "Ponyo", "Spirited Away", "My Neighbor ToToro", "Porco Rosso"
]

teen_movies = [
    "Bill & Ted's Excellent Adventure", "Bill & Ted's Bogus Journey", "American Pie", "SCREAM"
]

adult_movies = [
    "Terminator 2", "Aliens 2", "Casino", "Fight Club"
]

old_movies = [
    "RED", "The Good, The Bad, and The Ugly", "Bucket List", "No Country for Old Men"
]

if age <= 15:
    random.shuffle(kids_movies)
    print("Try watching", kids_movies[0])
elif 15 < age <= 23:
    random.shuffle(teen_movies)
    print("Try watching", teen_movies[0])
elif 23 < age < 50:
    random.shuffle(adult_movies)
    print("Try watching", adult_movies[0])
elif age >= 50:
    random.shuffle(old_movies)
    print("Try watching", old_movies[0])