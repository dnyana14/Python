#WAP to ask the user for their 3 favorite movies and store them in a list
movies = []
movie1 = input("Enter your first favorite movie: ")  

 #We can drectly append(add) input to the list using append method
 #movies.append(input("Enter your first favorite movie: "))
 #movies.append(input("Enter your second favorite movie: "))

movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")
#append method to add elements to the list
movies.append(movie1) #adds the first movie to the list
movies.append(movie2) #adds the second movie to the list    
movies.append(movie3) #adds the third movie to the list  

print("Your favorite movies are: ", movies)