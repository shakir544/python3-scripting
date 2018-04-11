# Python script to check the number of files, find duplicates, sizes of the files
import os
import sys
import shutil


# get the details of folder
if not len(sys.argv) > 1:
    print("Not enough number of args to filechecker")
    sys.exit(1)

sourcedir = sys.argv[1]

if os.path.isdir(sourcedir):
    # list the files in the directory
    files = os.listdir(sourcedir)

else :
    print(sourcedir + " not exists. Provide a directory to check the details")
    sys.exit(1)


def display(files):
    for count, file in enumerate(files):
        print("{0} - {1}".format(count,file))

