# Question 2 in Modules
import random


'''
you have the follow code

words = ["Python","two","car","house","PHP"]
you need to generate random password using 3 items from a list 

'''

words = ["Python","two","car","house","PHP"]
print("".join(random.SystemRandom().choice(words) for i in range(3)))