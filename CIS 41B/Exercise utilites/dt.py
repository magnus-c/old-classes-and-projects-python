import time
import datetime
import pendulum as dt

def yearsaway(date):
    given = date.year
    rightnow = dt.now().year
    difference = given - rightnow
    return difference

print("Time formatting ",25*'-')
# time formatting
q = dt.date(2050, 2, 3)
print(yearsaway(q))
