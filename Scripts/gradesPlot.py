#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:47:05 2020

@author: mads
"""

import numpy as np
import matplotlib.pyplot as plt 
from computeFinalGrades import computeFinalGrades

def gradesPlot(grades):
    #Tager numpy matrice, og danner to plots. Benytter gradesFinal til at beregne
    #finalgrades, der skal plottes i plot 1. 
    #Brug: Kald funktionionen, NB! Funktionen fjerner de to første søjler da 
    #Det antages, at disse består af studie nr. og navn. 
    
#________________________________Final grades_plt_____________________________
   gradesFinal = computeFinalGrades(grades)
    
   #Plotter histogram over vektoren FinalGrades, og sørger for at søjlerne bliver lige brede
   plt.hist(gradesFinal, bins=np.arange(min(gradesFinal), max(gradesFinal) + 2),align = "left",rwidth = 1, histtype="bar")
    
   plt.xticks([-3,0,2,4,7,10,12]) #Definerer hvilke ticks vi vil have på plot
    
   plt.xlabel("Karakterer")
    
   plt.ylabel("Antal karakterer givet")
    
   plt.title("Final Grades")
    
   plt.show() 
   
#___________________________Grades per assignment_____________________________
   
   #Fjerne de to første kolloner, da de ikke skal bruges i beregninger
   #Sikrer sig også alle værdier er floats 
   pure_grades = grades[:,2:].astype(np.float)
   
   #Laver en nulvektor på længde med søjlerne i matricen, da vi transposer den senere.
   x = np.zeros([len(pure_grades[:,0])])
   #Laver et array med en værdi på 0.
   x1 = np.array([0])

   #Mean af hver søjle, så det kan bruges til at plotte. 
   meanGrade = pure_grades.mean(0)
   #Tilføjer mean vektoren til et array med et nul, og sætter den nul værdi lig none,
   #for der ikke kommer punkt, og at mean grafen ikke starter på assignment 0.
   meanGrade = np.append(x1,meanGrade)
   meanGrade[0] = None
   
   #Tilføjer støj til dataen, så to punkter med samme værdi kan adskilles på plot 
   noise = np.random.uniform(low=-0.1, high=0.1, size=pure_grades.shape)
   gradesFinalplt = pure_grades + noise
   
   #Her transposer vi matricen for at få de korrekte karaktere til opgaven.
   #Hvis dette ikke var gjort, ville den tage alle assignments for en person, som assignment 1.
   gradesFinalplt = gradesFinalplt.transpose()
   
   #Vi tilføjer her matricen, på en nulvektor, for at få assignmentsne til at starte fra 1 og ikke 0
   gradesFinalplt = np.vstack([x,gradesFinalplt])
   #Desuden har vi lavet hele første række i matricen, som er nulrækken, lig None,
   #da der ellers ville komme punkter i scatterplottet.
   gradesFinalplt[0,:] = None
   
   #Laver et tomt array, som vi kan bryge til labels i legend
   lab = np.array([])
   
   
   #Laver det tommme array om til et array som indeholder "_nolegend_",
   #som gør vi ikke får dublicates i vores legend.
   #Den laver arrayet lige langt som den givne matrice, minus 1.
   for i in range(len(gradesFinalplt[0,:]) - 1):
       lab = np.append(lab,"_nolegend_")
       #lab = np.array(["_nolegend_","_nolegend_","_nolegend_","_nolegend_","Grades","Mean"])
   
   #Her sætter vi 2 nye værdier på lab, som er vores grades og mean.
   #Dette array bliver dermed lige langt med søjlerne på matricen
   lab = np.append(lab,"Grades")
   lab = np.append(lab,"Mean")
       
   #Plotter matricen som scatterplot, og plotter mean af punkterne.
   plt.plot(gradesFinalplt, ".b",label = "Grades") #Plotter karakter matricen, med blå punkter
   plt.plot(meanGrade,"-r",label = "Mean") #Plotter mean af karaktererne, som rød streg.
   plt.yticks([-3,0,2,4,7,10,12]) #Definerer hvilke ticks vi vil have på plot
   plt.xlabel("Assignment") #Kalder x-aksen for "Assignment"
   plt.ylabel("karakter") #Kalder y-aksen for "Karakter"
   plt.title("Grades Per Assignment") #Giver plottet et navn; "Grades Per Assignment"
   
   #tilføjer her en legend, så i kan se hvilke der er karakterer og hvilke der er mean.
   #sætter også legend uden for plottet
   plt.legend(labels = lab,bbox_to_anchor=(1,1))
   #Definere plottet som variabel.
   plt.grid()
   plt.show()
   













