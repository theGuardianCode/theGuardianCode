# This program was built to create folders for each of the inputed classes. Inside those folders ther are subfolders for each term. 

from msilib.schema import Directory
import os
from os import listdir
from os.path import isfile, join

inputingClass = True


classes = []

# Defines the function which creates the folders and sub-folders. Parent directory is where the subject folders will be located and directory is the sub-folder's directory.
def createTermFolders(subject):
    for i in range(4):
        directory = 'Term ' + str(i + 1)
        parent_dir = subject + "/"
        path = parent_dir + directory
        os.makedirs(path)

while True:
    
    startOptions = input("\nWould you like to create folders (1) or sort files (2)? ")
    
    if startOptions == "1":
        print("\nType the name of your class then hit enter to move to next line. When finished, type 'Done' then hit enter.")
        # Reads the user input from above and appends the class name to the end of the classes list. If the input reads "Done" then the loop will break.
        while inputingClass == True:
            classInput = input("Class name: ")
            if classInput == "Done":
                inputingClass = False
                break
            else:
                classes.append(classInput)
        # Loops through the list of classes creating folders and sub-folders for each one.
        for i in range(len(classes)):
            createTermFolders(classes[i])
        break
    elif startOptions == "2":
        print("Sorting files...")
        
        # Gets the working directory with all subject folders in it.
        currentDir = os.getcwd()
        # Was complicated to understand at first. In line 52 f is added to the list while iterating 
        # from 0 to the amount of files in the directory. f is only added to the list if the current object is a file.
        fileList = [f for f in listdir(currentDir) if isfile(join(currentDir, f))]
        # Removes the source code file and data file from the file list.
        fileList.remove("Organise.py")
            
        
        for i in fileList:
            if "(" and ")" in i:
                # This block of variables filters the file name from the path and extention
                classNum = fileList.index(i)
                currentSub = str(fileList[classNum])
                SubAndTerm = currentSub.split("(")
                justSubject = str(SubAndTerm[1])
                refinedSubject = justSubject.split(" ")
                FinalSubject = str(refinedSubject[0])
                
                # Variables for the term folders
                fileTerm = str(SubAndTerm[1]).split(")")
                justTerm = str(fileTerm[0])
                refinedTerm = justTerm.split(" ")
                FinalTerm = str(refinedTerm[1])
                
                # Moves the files to their matching subject and term folders
                os.replace(currentDir + "/" + i, currentDir + "/" + FinalSubject + "/Term " + FinalTerm + "/" + i)
                print("Moving " + str(i) + " to " + FinalSubject + " Term " +  str(FinalTerm))
            else:
                print("File location not specified")
        break
    print("\nInput is invalid")
    continue
