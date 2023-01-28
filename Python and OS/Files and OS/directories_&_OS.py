import os
# print(os.getcwd())   #current working directory
# print(os.listdir(os.getcwd()))

# https://docs.python.org/3/library/os.html

# https://docs.python.org/3/library/os.path.html

# https://en.wikipedia.org/wiki/Unix_time

#program to diffferentiate the directories and  files


def diff_dir_files(dir):
    for name in os.listdir(dir):
        fullname= os.path.join(dir,name)
        if os.path.exists(fullname):
            print(name," is a Directory")
        else:
            print(name," is a File")





#The create_python_script function creates a new python script in the current working directory
# , adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file
# . Fill in the gaps to create a script called "program.py".
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,'a+') as f:
    f.write(comments)
    print(f.read())
    filesize = os.path.getsize(filename)
  return(filesize)


