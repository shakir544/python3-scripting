# Demostrate the python code for Shallow copy
import copy


# Function to print the elements of list
def print_list(list):
    for item in list:
        print(item)


# create src & tar lists
src = [1, 2, 3, [4,5]]
tar = copy.copy(src)


print("Print src list before shallow copy")
print_list(src)

print("print tar list before modification")
print_list(tar)

tar[3][0] = 544

print("Print src list after shallow copy")
print_list(src)

print("print tar list after modification")
print_list(tar)