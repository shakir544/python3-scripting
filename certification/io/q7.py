# question 7 - Files IO

import csv

students = [["shakir",544],["gooty",5260],["shakeel", 56],["Shaffi",9]]

with open("test.csv","w") as f:
    w = csv.writer(f)
    w.writerows(students)

