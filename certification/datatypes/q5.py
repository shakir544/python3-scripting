# Question 5


'''
Function to print the lowest and highest grades
print("lowest grade and highest grade are %d and %d" % (grade1, grade2) 
'''


def find_the_grade(grades):
    grades.sort()
    return grades[0], grades[-1]


grades = [10,34,56,23,90,34]
grade1, grade2 = find_the_grade(grades)

print("lowest grade and highest grade are %d and %d" % (grade1, grade2) )
