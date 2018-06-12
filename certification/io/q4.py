# Question 4
import sys

sum = 0
for mark in range(2,range(len(sys.argv))):
    sum += float(sys.argv[mark])

print("".format(sys.argv))