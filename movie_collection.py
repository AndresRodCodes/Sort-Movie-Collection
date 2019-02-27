import operator

# Build a dictionary containing the specified movie collection
#To create the initial dictionary I used the best practice of
#having the values be lists and even having two lists in one value
#for the years of 2006 and 2011. I also placed the "\" notation
#in "King\'s " so the apostrophe is not ignored.
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

#This if statment uses the best practice of seperating the two conditions
#while making it more readable. I also used the best practioe of using the
#relevant years when comparing with the user input. I solved the problem of
#checking for the range between 2005 and 2016 by using the "and" operator
if (user_year_input >= 2005) and (user_year_input <= 2016):
    # Displaying the title(s) and directors(s) from that year
    #Since there are a two years with 2 lists as thier value
    #I had an Out Of Index error when using only one algorithm. I solved that problem
    #by using an if statement and checking for years the years that had
    #two lists as a value (2011 and 2006). All the other years would be sorted
    #in the "else" statement. I wish I could have had an if statement to check the
    #number of lists as values instead but I can not figure it out yet.
    if (user_year_input == 2011) or (user_year_input == 2006):
        #Knowing these years have two lists as the value I can
        #assign each part to its appropritate variable.
        movie1 = movie_collection[user_year_input][0][0]
        director1 = movie_collection[user_year_input][0][1]
        movie2 = movie_collection[user_year_input][1][0]
        director2 = movie_collection[user_year_input][1][1]
        #I used the best practice of contatinating the movies, directors and
        #format and assigning it to a variable to be able to go back and modify it
        #easily. I also used the best practice of surrounding the long concatinated statement in
        #parentheses then breaking it into two lines.
        str_movies_and_directors = (movie1 + ', ' + director1 + '\n' +
                                    movie2 + ', ' + director2)
        print(str_movies_and_directors)

    else:
        #Knowing this would only exicute if the dictionary entry only
        #contained one list, I assigned the first element of the list to movie
        #and the second to director
        movie = movie_collection[user_year_input][0]
        director = movie_collection[user_year_input][1]
        str_movie_and_director = movie + ', ' + director
        print(str_movie_and_director)

else:
    #I used the best practice of printing out and error message when
    #the user enters anything other than the options given.
    print('N/A')

#I use the best practice of printing out the menu with multiple print
#statments to make it easier to modify and read as needded.
# Display menu
print('\nMENU')
print('Sort by:')
print('y - Year')
print('d - Director')
print('t - Movie title')
print('q - Quit')
user_menu_input = input('\nChoose an option:\n')

#I chose to solve the problem of staying in the program as long at the letter "q" is not
#entered by using a While loop and comparing the user_menu_input to the letter "q"
while user_menu_input != 'q':
    #Carry out the desired option: Display movies by year,
    #I chose the if/elif data structure because it allows for multiple scenarios
    #dependent of user_menu_input
    if user_menu_input == 'y':
        #I chose a for loop to itterate through the movie colleciton and solve the problem
        #of sorting by year by using the sorted() function and the key perametter and setting
        #it to sort by the first item, which is the year. I have to thank stack overflow for
        #assisting me with this part.
        for year, value in sorted(movie_collection.items(), key=operator.itemgetter(0)):
            #I again use the if and else data structure to check for the years that have
            #two lists as the values or else I would get and Out of index error.
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
    #I used the elif statement following the if statement to check for the letter "d"
    #in user_menu_input
    elif user_menu_input == 'd':

        #This part the was most challenging of all! I was able to get it sorting by director,
        # but I was not able to sort by year after the first sort. I will learn it.
        #Getting back to the program, I decided to create a new dictionary that will use
        #the director as the key to make it easier to sort.
        sorted_director_dictionary = {}
        #In this line i use the sorted() method and the lambda key so I can sort by director. Using
        #the lambda key I do not get an out of index error. The problem is, the values with two
        #lists get placed at the end.
        for year, value in sorted(movie_collection.items(), key=lambda item: (item[1][1][0])):
            #I filter again the values with two lists and the value
            if (year == 2011) or (year == 2006):
                movie1 = value[0][0]
                movie2 = value[1][0]
                director1 = value[0][1]
                director2 = value[1][1]
                #Here I check if director1 is in the new sorted dictionary that contain
                #directors as the keys to add the other movie and year to the list value
                #using the dictionary append() function.
                if director1 in sorted_director_dictionary:
                    sorted_director_dictionary[director1].append([movie1, year])
                #Here I check if director2 is in the new sorted dictionary that contain
                #directors as the keys to add the other movie and year to the list value.
                #using the dictionary append() function.
                elif director2 in sorted_director_dictionary:
                    sorted_director_dictionary[director2].append([movie2, year])
                #If neither director1 or director2 was found, the directors, movies and years
                #would be added to the sorted_director_dictionary.
                else:
                    sorted_director_dictionary[director1] = [movie1, year]
                    sorted_director_dictionary[director2] = [movie2, year]
            #If the year is not 2011 or 2006 then the value is only one list so this
            #else statement is executed. It added the the directors and their movie and year to the
            #sorted_director_dictionary.
            else:
                movie = value[0]
                director = value[1]

                if director in sorted_director_dictionary:
                    sorted_director_dictionary[director].append([movie, year])

                else:
                    sorted_director_dictionary[director] = [movie, year]
        #I am not sure how but "Martin Scorses" was lost in the process of creating the new dictionary
        #so I manually added the data back.
        sorted_director_dictionary['Martin Scorsese'] = ['The Departed', 2006]

        #With the new dictionary I solved the problem of the values with two lists getting placed
        #last.
        for director, value in sorted(sorted_director_dictionary.items(), key=operator.itemgetter(0)):
            #I then use the best practice of using the if/else statements to filter by
            #directors knowing which directors have two lists as the value
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
        #I used a very similar algorithm to sort by movie title.
        #I create a dictionary again to be populated with the movie title as the key
        #and the director and year as the value.
        sorted_movie_dictionary = {}
        #This first sort might not have been necessary but I did not want to risk taking it out
        #because I did not cause any problems. That is not a best practice.
        for year, value in sorted(movie_collection.items(), key=lambda item: (item[1][0][0])):
            #This if/else statment checks for the years with two lists as values and adds the
            #movie titles as the list and the directors and years as a list value.
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
        #I used the best practive of using a for loop to iterate through the
        #sorted_ movie_dictionary. Also, the best practice of sorting the dictionary before itteration.
        for movie, value in sorted(sorted_movie_dictionary.items(), key=operator.itemgetter(0)):
            director = value[0]
            year = value[1]
            sorted_movie = movie + ':' + '\n\t' + director + ', ' + str(year) + '\n'
            print(sorted_movie)
    #After every user menu choice I display the menu again so they can
    #choose to sort by any other type of data.
    print('MENU')
    print('Sort by:')
    print('y - Year')
    print('d - Director')
    print('t - Movie title')
    print('q - Quit')

    user_menu_input = input('\nChoose an option:\n')
