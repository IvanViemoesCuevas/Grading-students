# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:26:10 2020

@author: Iván
"""
# PrintErrors prints all errors contained in arrays from DataLoad directly.
# Each array is checked for size, if it's empty the program will notify the user
# that their document is free of errors.
# This function will only output to console. All returns are print statements.

from DataLoad import LoadData
import numpy as np


def PrintErrors(DupErr, IDErr, NameErr, GradeErr):

    print("Checking for errors:")

    # DupErr printing. sep='' erases whitespaces from print()
    if DupErr.size == 0:
        print("Duplication check. No Errors")
    else:
        for i in range(DupErr.shape[1]):
            print(
                "Duplicate ID: ",
                DupErr[0, i],
                ", line: ",
                DupErr[2, i],
                ", ",
                DupErr[1, i],
                " instances.",
                sep="",
            )

    # IDErr printing.
    if IDErr.size == 0:
        print("Missing ID's check. No Errors")
    else:
        for i in range(IDErr.size):
            print("Missing ID: line ", IDErr[i], ".", sep="")

    # NameErr printing.
    if NameErr.size == 0:
        print("test")
    else:
        for i in range(NameErr.size):
            print("Missing Name: line ", NameErr[i], ".", sep="")

    # GradeErr printing
    if GradeErr.size == 0:
        print("Grade out of bounds check. No Errors", sep="")
    else:
        for i in range(GradeErr.size):
            print("Incorrect grade found: line ", GradeErr[i], ".", sep="")

    # Checking for zero errors. \line break
    if (
        DupErr.size == 0
        and IDErr.size == 0
        and NameErr.size == 0
        and GradeErr.size == 0
    ):
        print("No errors found in document. You can now proceed.")
    else:
        return print("Error check done.")


# Debugging:
# LoadData = LoadData("testdata.csv")
# print(PrintErrors(LoadData[3],
#                   LoadData[4],
#                   LoadData[5],
#                   LoadData[6]))
