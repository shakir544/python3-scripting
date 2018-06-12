# question 2 :

amount = input("enter amount")
# The user enters 322346.1234 which statement print the following output
# 322,346.57

print("{:,0.2f}".format(float(amount)))