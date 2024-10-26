'''
Magnus Chiu
CIS 41A Spring 2022
Unit D, Problem D
'''
from collections import namedtuple
triangle_number = [x*(x+1)/2 for x in range(11) if x > 0];
print("First 10 Triangle numbers:");
print(triangle_number);

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"};
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"};
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"};
print("Students in all three classes:",sorted((class1.intersection(class2).intersection(class3))));
print("All students:",sorted((class1.union(class2).union(class3))));
print("Students in class1 but not class2 or class3:",sorted((class1.difference(class2).difference(class3))));
class2not1 = [x for x in class2 if x not in class1];
print("Students in class2 but not class1", class2not1);


movieInfo = ("Casablanca", 1942, "romantic drama");
(title, year, genre) = movieInfo;
print("The genre of my favorite movie is:", genre);

Movie = namedtuple("Movie", "title year genre");
movie = Movie("Casablanca", 1942, "romantic drama");
print("My favorite movie is:",movie.title);

Moviestars = namedtuple("Moviestars","title year genre stars");
favoritemovie = Moviestars("Casablanca", 1942, "romantic drama", ["Humphrey Bogart", "Ingrid Bergman"]);
favoritemovie.stars.append("Claude Rains");
print("My favorite star is:",favoritemovie.stars[1]);
print(favoritemovie);

'''
Execution results:
First 10 Triangle numbers:
[1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0]
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
Students in class2 but not class1 ['Sasha', 'Hiroto']
The genre of my favorite movie is: romantic drama
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''