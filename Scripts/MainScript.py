#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:53:34 2020

@author: Iván
"""

import numpy as np
from displayMenu import displayMenu
from DataLoad import LoadData
from gradesPlot import gradesPlot
from ListGrades import listGrades
from computeFinalGrades import computeFinalGrades
from PrintErrors import PrintErrors


# Funktionerne er implementeret sammen.
# _______________________________Menuvalg______________________________________

# Menu options:
menuItems = np.array(
    [
        "Load data",
        "Check data",
        "Generate plots",
        "Show list grades",
        "Quit",
        "Export list as CSV",
    ]
)

# Creates a variable with an empty string for saving user input
filename = ""

# Skal spørge bruger med det samme om at indlæse fil. Og gemmer filnavn i variabel
filename = input("Please write name of CSV. file:")

# Gemmer outputs fra LoadData funktion, da de returneres som liste
Output = LoadData(filename)


# CSV filen fra LoadData Gemmes i variabel

if Output == False:
    print("Please try again.")
else:
    CSV = Output[1]
    finalGrades = computeFinalGrades(Output[1])
    print(CSV)
    # Printer antal studerende:
    print("Number of students:" + str(len(finalGrades)))
    # Printer antal opgaver:
    print("Number of assignments:" + str(len(CSV[0]) - 2))

while True:
    choice = displayMenu(menuItems)

    # Load ny data funktion
    if choice == 1:
        filename = input("Please write name of new CSV. file:")
        Output = LoadData(filename)
        # 2. output fra LoadData er CSV filen.
        if Output == False:
            print("Please try again.")
        else:
            CSV = Output[1]
            finalGrades = computeFinalGrades(Output[2])
            print(CSV)
            # Printer antal studerende:
            print("Number of students:" + str(len(finalGrades)))
            # Printer antal opgaver:
            print("Number of assignments:" + str(len(CSV[0]) - 2))

    elif choice == 2:
        if Output == False:
            print("No file found")
        else:
            # Kalder PrintErrors der printer de fundne fejl i datasættet
            print("")
            PrintErrors(Output[3], Output[4], Output[5], Output[6])
            print("")

    # Plotter den givne data
    elif choice == 3:
        if Output == False:
            print("No file found")
        # Gemmer output fra plot funktion som liste
        else:
            # Outputter plotsne der er dannet på baggrund af den givne data
            # index 1 i output er vores np version af den givne data.
            gradesPlot(Output[2])

    # Printer den fuldstændige liste, af karakter med finalgrades
    elif choice == 4:
        if Output == False:
            print("Please load file first (menu option 1)")
        else:
            print(listGrades(finalGrades, Output[0]))
            print(
                "To see the full dataset, change prompt options, or export to CSV (Choice 6)"
            )

    # Stopper program
    elif choice == 5:
        break

    elif choice == 6:
        if Output == False:
            print("Please load file first (menu option 1)")

        else:
            # Gemmer først listGrades som variabel.
            List = listGrades(finalGrades, Output[0])
            # Exporterer listGrades som CSV fil
            List.to_csv("ExportetFile.csv", index=False)
            # Bruger feedback
            print("File has been exportet to program folder")


# ___________________________________________________________________________

print("Program has closed ")
