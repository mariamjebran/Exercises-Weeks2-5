# Write your code here
from re import A


def divisible_by_3(*args):
    final_list = []
    for number in args:
        if number % 3 == 0:
            final_list.append(number)
    return final_list

divisible_by_3(2 , 3, 5, 6, 9)