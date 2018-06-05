# question 3
import pickle

course_count = [["c++","24"],["Java","32"],["Python","38"], ["Java Script","29"],["C#","40"] ]

with open("lang.bin","wb") as f:
    pickle.dump(course_count,f)

with open("lang.bin","rb") as f :
    course_count2 = pickle.load(f)
