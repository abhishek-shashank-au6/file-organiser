#  DSA Python Project

* ### Title: File-Organiser
* ### GitHub Uri: [Repo link](https://github.com/abhishek-shashank-au6/file-organiser)

___

* ### Developer: **Abhishek Shashank**
* ### Instructor: **Mr. Priyesh Srivastava**
* ### Mentor: **Mr. Saidul Mondal**

___

## Overview: 

* ### A basic implementation of a File Organiser in Python

* ### Command Line Interface present for User Instructions

* ### The User can arrange the files according to the Size, Extension and Date Modified

* ### The Organised Files will be present in a folder named "Organised" inside the Actual Folder

___

## Features:

* ### Organise Files By Extensions into Different Folders inside the Actual Folder

* ### Organise Files By Size into Folders named 'Small' , 'Medium' and 'Large'

* ### Organise Files By Latest Modified Date with Folders named by the Date Modified Itself

___

## Modules Used:

* ### **OS** Module for Interacting with Files

* ### **SHUTIL** Module for copying and deleting files

* ### **ARGPARSE** Module for manipulating the CLI

* ### **DATETIME** Module for getting the Modification Timestamp for Files

___

## Pre-Requisites:

* ### Command Line Parsing

* ### File Handling in Python

* ### Recursion

___

## Approach:

* ### Create different folders based on File Extension, Size or Date Modified based on the User Instruction

* ### Segregate into different folders using dictionaries

* ### Create the map of file types into their respective folders

* ### Create a function to filter file types into their respective folders

* ### Use **OS** module of python to recursively list out all the files that are present in the folders with their relative and absolute path

* ### A folder named "Organized" is created inside which all the sub-folders based on the respective type are present

* ### Using Shutil module of python, move all the files into the accordingly created sub-folders

___

## Execution

* ### The execution command has two Positional Arguments

* ### --d=directory where directory specifies the absolute path of the directory to be organised.

* ### --o=option where option specifies the choice of organising the files

* ### The choice of option is **ext** for Organising based on File Extension

* ### The choice of option is **size** for Organising based on File Size

* ### The choice of option is **date** for Organising based on Modified Date

* ### If no value is provided for the option argument then by default the files are organised by their Extension Type

* ### If the Python Script File is present in the directory to be organised then the directory argument could be avoided

    **python3 organiser.py --o=option**

* ### This means that if no value for the directory argument is provided then the files present in the current working directory are organised

* ### The Python Script File needs to be present in the Currently Navigated Directory in the Command Line Tool and then it can execute the script for any desired folder by providing its absolute path 
    **python3 organiser.py --d=directory_path --o=option**

___

## Future Scope

* ### Adding Options for Organisation like Sorting in Alphabetical Order

* ### Different Options for Deleting or Reaming Files can be Added

* ### Graphical User Interface can be Deceloped for this Application

___