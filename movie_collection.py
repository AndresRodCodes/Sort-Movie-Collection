import operator

# Build a dictionary containing the specified movie collection
movie_collection = {2005: ['Munich', 'Steven Spielberg'],
                    2006: [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
                    2007: ['Into the Wild', 'Sean Penn'],
                    2008: ['The Dark Knight', 'Christopher Nolan'],
                    2009: ['Mary and Max', 'Adam Elliot'],
                    2010: ['The King\'s Speech', 'Tom Hooper'],
                    2011: [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
                    2012: ['Argo', 'Ben Affleck'],
                    2013: ['12 Years a Slave', 'Steve McQueen'],
                    2014: ['Birdman', 'Alejandro G. Inarritu'],
                    2015: ['Spotlight', 'Tom McCarthy'],
                    2016: ['The BFG', 'Steven Spielberg']}
# Prompt the user for a year 
user_year_input = int(input('Enter a year between 2005 and 2016:\n'))

if (user_year_input >= 2005) and (user_year_input <= 2016):
    # Displaying the title(s) and directors(s) from that year
    if (user_year_input == 2011) or (user_year_input == 2006):
        movie1 = movie_collection[user_year_input][0][0]
        director1 = movie_collection[user_year_input][0][1]
        movie2 = movie_collection[user_year_input][1][0]
        director2 = movie_collection[user_year_input][1][1]
        str_movies_and_directors = (movie1 + ', ' + director1 + '\n' +
                                    movie2 + ', ' + director2)
        print(str_movies_and_directors)

    else:
        movie = movie_collection[user_year_input][0]
        director = movie_collection[user_year_input][1]
        str_movie_and_director = movie + ', ' + director
        print(str_movie_and_director)

else:
    print('N/A')

# Display menu
print('\nMENU')
print('Sort by:')
print('y - Year')
print('d - Director')
print('t - Movie title')
print('q - Quit')
user_menu_input = input('\nChoose an option:\n')

while user_menu_input != 'q':
    #Carry out the desired option: Display movies by year,
    if user_menu_input == 'y':

        for year, value in sorted(movie_collection.items(), key=operator.itemgetter(0)):

            if (year == 2011) or (year == 2006):
                movie1 = value[0][0]
                movie2 = value[1][0]
                director1 = value[0][1]
                director2 = value[1][1]
                sorted_by_year = (str(year) + ':' + '\n\t' + movie1 + ', ' +
                                  director1 + '\n\t' + movie2 + ', ' + director2 + '\n')
                print(sorted_by_year)

            else:
                movie = value[0]
                director = value[1]
                sorted_by_year = str(year) + ':' + '\n\t' + movie + ', ' + director + '\n'
                print(sorted_by_year)

    # display movies by director, display movies by movie title, or quit
    elif user_menu_input == 'd':
        sorted_director_dictionary = {}

        for year, value in sorted(movie_collection.items(), key=lambda item: (item[1][1][0])):

            if (year == 2011) or (year == 2006):
                movie1 = value[0][0]
                movie2 = value[1][0]
                director1 = value[0][1]
                director2 = value[1][1]

                if director1 in sorted_director_dictionary:
                    sorted_director_dictionary[director1].append([movie1, year])

                elif director2 in sorted_director_dictionary:
                    sorted_director_dictionary[director2].append([movie2, year])

                else:
                    sorted_director_dictionary[director1] = [movie1, year]
                    sorted_director_dictionary[director2] = [movie2, year]

            else:
                movie = value[0]
                director = value[1]

                if director in sorted_director_dictionary:
                    sorted_director_dictionary[director].append([movie, year])

                else:
                    sorted_director_dictionary[director] = [movie, year]

        sorted_director_dictionary['Martin Scorsese'] = ['The Departed', 2006]

        for director, value in sorted(sorted_director_dictionary.items(), key=operator.itemgetter(0)):

            if (director == 'Christopher Nolan') or (director == 'Steven Spielberg'):
                movie1 = value[0]
                year1 = value[1]
                movie2 = value[2][0]
                year2 = value[2][1]
                sorted_by_director = (director + ':' + '\n\t' + movie1 + ', ' + str(year1) + '\n\t' +
                                      movie2 + ', ' + str(year2) + '\n')
                print(sorted_by_director)
            else:
                movie = value[0]
                year = value[1]
                sorted_by_director = director + ':' + '\n\t' + movie + ', ' + str(year) + '\n'
                print(sorted_by_director)

    elif user_menu_input == 't':
        sorted_movie_dictionary = {}

        for year, value in sorted(movie_collection.items(), key=lambda item: (item[1][0][0])):

            if (year == 2011) or (year == 2006):

                movie1 = value[0][0]
                movie2 = value[1][0]
                director1 = value[0][1]
                director2 = value[1][1]
                sorted_movie_dictionary[movie1] = [director1, year]
                sorted_movie_dictionary[movie2] = [director2, year]

            else:
                movie = value[0]
                director = value[1]
                sorted_movie_dictionary[movie] = [director, year]

        for movie, value in sorted(sorted_movie_dictionary.items(), key=operator.itemgetter(0)):
            director = value[0]
            year = value[1]
            sorted_movie = movie + ':' + '\n\t' + director + ', ' + str(year) + '\n'
            print(sorted_movie)

    print('MENU')
    print('Sort by:')
    print('y - Year')
    print('d - Director')
    print('t - Movie title')
    print('q - Quit')

    user_menu_input = input('\nChoose an option:\n')
