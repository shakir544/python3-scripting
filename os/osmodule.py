import os
import shutil

#https://hplgit.github.io/edu/ostasks/ostasks.pdf

# Check if the folder is existing, if not Create a folder or directory
if not os.path.isdir('mydirs'):
    os.mkdir('mydirs')

# Create a intermediate folder
foldername = os.path.join(os.environ['HOME'], 'python', 'test')


if not os.path.isdir(foldername) :
    os.makedirs(foldername)

# Move to a folder
currentdir = os.getcwd()  # get name of current directory
os.chdir(foldername)
print(os.getcwd())
os.chdir(currentdir)
print(os.getcwd())

# remove directories using shutil
shutil.rmtree(foldername)
shutil.rmtree('mydir')
shutil.rmtree('mydirs')