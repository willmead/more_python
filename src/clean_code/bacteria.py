"""
Bacteria
========

Write some code to print out how many bacteria will
exist on a surface after a certain number of minutes.

You will need 3 variables:

- A variable that contains the starting number of bacteria (e.g. 10)
- A variable containing the total length of time they have
    to reproduce (e.g. 120mins)
- A variable that says how often they 'split' (e.g. every 10 minutes)

I recommend writing a 'for loop' to double the number of bacteria every so often.

To double a number:

 number *= 2

REMEMBER TO WRITE CLEAN CODE!!!
"""


initial_bacteria = 10
time_limit = 260
time_between_splits = 10

total_bacteria = initial_bacteria

for time in range(0, time_limit, time_between_splits):

    total_bacteria *= 2
    print(f"{time} mins: {total_bacteria} bacteria")

    if time % 120 == 0:
        total_bacteria *= 0.01
    
    




























    
    
