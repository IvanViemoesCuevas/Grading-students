#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:02:27 2020

@author: Iván
"""

import numpy as np
import pandas as pd
from roundGrade import roundGrade


def computeFinalGrades(grades):
    # Tager numpy matricen indeholdende elevernes karakterer for hver assignment.
    # Output: er gradesFinal, der er et array indeholdende de endelige karakterer for eleverne
    # Brug: var = computeFinalGrades(grades)

    # I denne funktion skal kollonerne Name og Student ID ikke bruges der for fjernes de, og de konverteres til floats.
    grades = grades[:, 2:].astype(np.float)

    # Danner et array af 0, med samme længde som matrix højde.
    gradesFinal = np.zeros(len(grades))

    # Hvis der kun er 1 assignment gradesFinal være det array så være final Grade
    if (len(grades[0])) == 1:
        gradesFinal = grades[:, 0]

    else:
        # Looper gennem de enkelte rows i matricen:
        for i in range(len(grades)):

            # Checker om -3 er i rowen og sætter Finalgrade til -3 hvis True
            if -3 in grades[i, :]:
                gradesFinal[i] = -3

            # Tager mean af array og sætter til gradesFinal
            else:
                # Fjerner den laveste værdi i vektoren og gemmer array i en "midlertidlig" variabel
                g = np.delete(grades[i, :], grades[i, :].argmin())
                # Beregner mean af karakter for den givne elev, og indsætter på tilsvarende plads
                # i GradesFinal
                gradesFinal[i] = np.round(np.mean(g), decimals=1)

    # Bruger funktionen roundGrade til, at afrunde karakterlisten til nærmeste karakter:
    gradesFinal = roundGrade(gradesFinal)

    return gradesFinal
