# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.


# import 'random' library for random numbers
import random

# creating a list of 100 random numbers from 0 to 1000
rand_list = random.sample(range(0, 1000), 100)

# an empy list for a sorted list
odd_numbers = []
even_numbers = []
# creating a sorted list
sorted_list = sorted(rand_list)
# searching the odd numbers from sorted list
for i in sorted_list:
    # checking the number whether the number is  an odd number
    if i % 2 != 0:
        odd_numbers.append(i)
    # if the number is not odd, adding the number to list_of_even numbers
    else:
        even_numbers.append(i)
# print the average value of the list with the odd numbers, the sum of all the numbers in the list divide by length of
# the numbers of the list
print(f'The average value of odd numbers is {sum(odd_numbers) / len(odd_numbers)}')
# print the average value of the list with the even numbers the sum of all the numbers in the list divide by length
# of the numbers of the list.
print(f'The Average value of the even numbers is {sum(even_numbers) / len(even_numbers)}')
