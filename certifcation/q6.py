# question 6

'''
You need to add the code to raise the error while preserving the stack trace
which line of code will you use ? 

1) raise ValueError("Error division by Zero") 
2) raise ValueError(e) 
3) raise 
4) raise as e
'''

try:
    x = 1/0
except Exception as e:
    print(e)
    raise

