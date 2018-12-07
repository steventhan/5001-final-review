from typing import List
"""
1. Design a function to convert in-place any list to a list of integers. 
Non-numeric types are converted to 0, numeric types are converted to integers.
Example:
[1, 5.0, "str"] -> [1, 5, 0]
["s", 42, True] -> [0, 42, 0]
"""

def convert_to_int_list(lst):
    pass

"""
2. Design a function that flattens a 2D list.
Example:
Input: [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
Output: [1, 2, 3, 4, 5, 6, 7 , 8, 9]
"""

def flatten_2d_lst(lst):
    pass


"""
3. Write a function that reverse a string and double a letter recursively.
Example:
Input: lst = [1, 3, 2, 8, 3, 1], element = 3
Output: 1
"""

def reverse_and_double_string(string, letter):
    pass


"""
4. Consider the class GuineaPig below. Design a function that takes a list of
guinea pigs and gives those that have favorite level greater than or equal to 3.
Do this recursively.
"""

class GuineaPig:
    def __init__(self, name, fav_level):
        self.name = name
        self.fav_level = fav_level

