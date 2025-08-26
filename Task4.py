import json
file = open('Sic/Tasks/movies.json', 'r') 
x = json.load(file)
file.close()

def add_movie():
    title = input("Enter the title of the movie: ")
    year = input("Enter the year of the movie: ")
    genre = input("Enter the genre of the movie: ")
    new_movie = {
        "title": title,
        "year": year,
        "genre": genre
    }
    x.append(new_movie)  # append first

    with open('Sic/Tasks/movies.json', 'w') as file_write:
      json.dump(x, file_write, indent=4)  

    print("New movie added successfully!")

print("welcome to IMDB elghalaba version")
choice = input("Do you want to search for a movie, or add a new movie?")

if choice == "add":
    add_movie()

else:
    movie = input("Enter the title of the movie you want to search for: ")
    if movie in x:
        print("Movie found!")
        print(movie + 'was made in' + movie.year + "and it's a(an)" + movie.genre + "movie")
    else:
        print("Movie not found!")
    if input("Do you want to add this movie? (yes/no)") == "yes":
        add_movie()
    else:
        print("Thank you for using IMDB elghalaba version!")