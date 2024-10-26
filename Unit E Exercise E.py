'''
Magnus Chiu
CIS 41A Spring 2022
Unit E, Exercise E
'''
scifi = ["Alien", "Solaris", "Inception", "Moon"];
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"];
name = str(input("Please enter a movie title: "));
if name in scifi:
    print(name, "is a scifi movie.");
    
elif name in comedy:
    print(name, "is a comedy movie.");
    
else:
    print("Sorry, I don't know what kind of movie", name, "is.");
    
print();

for num in range(10, -1, -2):
    print(num);
    
print();

movies = {"The Wizard of Oz":1939, "The Godfather":1972, "Lawrence of Arabia":1962, "Raging Bull":1980};

for i in sorted(movies):
    print(i,"was made in", movies[i]);
    
    
    
'''
Execution results (after all 3 tests): 
Please enter a movie title: Moon
Moon is a scifi movie.
Please enter a movie title: Superbad
Superbad is a comedy movie.
Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.

10
8
6
4
2
0

Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939
'''