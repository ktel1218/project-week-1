"""
1. Create 26 directories in the current directory, one for each letter 
of the alphabet:

2. Loop through all the files in the original_files directory, and 
organize each of those files into the directory that their name 
starts with.
Helpful modules:
    #os.listdir(".") lists the directory of the current file
    #os.mkdir("path")
    #os.chdir("..") changes directory up one
    #os.path.exists("path") check if path exists/ has basic permissions
    #shutil.move(src, dest/) moves/renames. dest/ cant already exist?
"""
from os import listdir, mkdir, chdir, path
from shutil import copy

def main():
    
    create_dirs()

    organize_files()


def create_dirs():
    #1. create directories a - z:
    for i in "abcdefghijklmnopqrstuvwxyz":
        mkdir("./%s" % i)

def organize_files():
    #2. Loop through files in original_files dir and put them into 
        #correct directory
    filelist = listdir("./original_files")


    for i in range(len(filelist)):
        first_letter = filelist[i][0]
        if path.exists("./%s" % first_letter):
            copy("./original_files/%s" % filelist[i], "./%s" % first_letter)

main()
