# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:51:35 2020

@author: Iván
"""

#LoadData takes the string input field from main corresponding to a CSV file in the same
#directory as the program. LoadData is responsible for parsing this CSV file for use 
#in the rest of the program. All error handling is checked here and outputted along
#with the CSV file in DataFrame and numpy format.
import numpy as np
import pandas as pd
import os.path
from roundGrade import roundGrade


def LoadData(filename):
    
#Check if file exists using the os.path module

    #If exists/ read file and convert to numpy
    if os.path.isfile(filename):        
        #Keep_default_na = false makes sure panda doesn't read empty cells as NaN, 
        #but rather empty strings "". For use in error handling.
        
        #The CSV file is saved as a DataFrame, Numpy array and "rounded" array (CSVr) with fixed grades.
        CSV = pd.read_csv(filename,keep_default_na = False) 
        CSV = CSV.to_numpy()
        
        CSVr = pd.read_csv(filename,keep_default_na = False) 
        CSVr = CSVr.to_numpy()
        
        CSVDataFrame = pd.read_csv(filename,keep_default_na = False) 
    else:
        print("File not found! Remember to specify .csv - Returning to main menu.")
        return False
    
    #CSV dim. size
    Len = len(CSV[:,0])
    LenRow = len(CSV[0,:])

    #Duplicate ID's checker
    IDdup = np.unique(CSV[:,0],0,0,1)
    DupItems = IDdup[0]
    DupInt = IDdup[1]
    
    Index = np.where(DupInt > 1)
    
    #DupErr is a three dim. array with ID, ID pos, ID dup. amount.
    DupErr = np.array([[],[],[]],int)
    for i in range(Len):
        for j in range(len(DupItems[Index])):
            if CSV[i,0] == DupItems[Index][j]:
                DupErr = np.append(DupErr, [[CSV[i,0]],[DupInt[Index][j]],[i]], axis = 1)

    # Missing ID's
    # This is where keep_default_na = False comes in use
    IDErr = np.array([],int)
    for i in range(Len):
        if CSV[i,0] == "":
            IDErr = np.append(IDErr, [i])
    
    #Missing Name
    NameErr = np.array([],int)
    for i in range(Len):
        if CSV[i,1] == "":
            NameErr = np.append(NameErr, [i])
            
    #Grade errors  
    Index2 = np.array([-3,0,2,4,7,10,12],int)
    GradeErr = np.array([],int)
     
    #For loop that checks for wrong grades with Index2
    for j in range(Len): 
        #Range -2, because of slicing in CSV array
        for i in range(LenRow - 2):
            if CSV[j,2:][i] not in Index2:
                GradeErr = np.append(GradeErr,[j])   
    GradeErr = np.unique(GradeErr)
    
    #Round with roundGrade function
    for i in range(Len):
        CSVr[:,2:][i] = roundGrade(CSVr[:,2:][i])

    #Returned as list for easy use in main script, check "Output[]"
    return [CSVDataFrame, CSV, CSVr, DupErr, IDErr, NameErr, GradeErr]

#For debugging:
#print(LoadData("testdata.csv"))
#[CSV, CSVr, DupErr, IDErr, NameErr, GradeErr]
























