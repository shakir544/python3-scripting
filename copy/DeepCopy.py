#!/usr/bin/python

# Python code demostrate copy functions

import copy

# custom function to print the elements in list


def print_list(list):
    for item in list:
        print(item)


# initialize a list
src = [1,2,3,4,5]

# using deep copy to copy
tar = copy.deepcopy(src)

# append a number in tar list
tar.append(6)

# print both src and tar list
print("Print src list ")
print_list(src)

print("print tar list")
print_list(tar)



