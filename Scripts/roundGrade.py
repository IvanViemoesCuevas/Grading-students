#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:17:47 2020

@author: Iván
"""
import numpy as np

# Funktion der afrunder det givne array af karakterer til karakterskala
def roundGrade(grades):
    # Input: np array, indeholdende vilkårlige tal
    # Output: Et afrundet array, der er rundet ifht. 7 trinsskalaen
    # Brug: Kald funktionen og indsæt np.array kun med numeriske værdier

    # Definerer 7 trinsskalen
    Skala = np.array([12, 10, 7, 4, 2, 0, -3])

    # Man trækker grades array fra Skala array pr. element og får en matrix ud med afstanden
    # til de forskellige karakterer ifht. input.
    afstand = np.subtract.outer(grades, Skala)

    # abs giver absolut værdien af vores matrix. Argmin giver indexet på den laveste værdi i rækkerne
    index = np.argmin(abs(afstand), axis=1)

    # Nu benytter vi arrayet y der indeholder indexet af hvilken karakterer vores grades array elementer var tættest på
    # Vha. Indexering
    gradesRounded = Skala[index]

    return gradesRounded


# print(roundGrade(np.array([8.4,9.8,1.1,9.9,2,-1.5,10.9])))

