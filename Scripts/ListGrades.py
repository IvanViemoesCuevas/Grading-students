#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:55:01 2020

@author: Iván
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 



def listGrades(finalgrades,CSV):
    #Input: Tager pd dataframe som input og array med final grades
    #Output: Outputter en pd df, med de endelige karakterer som sidste søjle
    #og rækerne sorteret i alfabetisk rækkefølge 
    #Brug, kald funktionen i mainscript, og giv krævede inputs
    #NB! For filer, med mange assignments kan der være problemer med, at displaye
    #hele dataframen. Juster evt. indstillinger for prompt, eller brug funktion til 
    #at eksportere filen som csv. 
    
    #Titles are extracted from the CSV
    Titles = CSV.columns.tolist()
    
    CSV_np = CSV.to_numpy()
    
    #Tilføjer titlen FinalGrades
    Titles.append("Finalgrade")
    
    #Konverterer listen til np array
    Titles = np.array(Titles)    
    
    #Først omdannes finalgrades arrayet til, 2d array
    finalgrades = np.array(finalgrades)[np.newaxis]
    
    #Final grades listen transponeres og tilføjes som sidste søjle i matricen CSV
    GradeList = np.concatenate((CSV_np, finalgrades.T), axis = 1)
    
     
    # Nu sorteres matricen i alfabetisk rækkefølge efter navn der står i 2 søjle 
    Gradelist_order = GradeList[np.argsort(GradeList[:, 1])]
    
    #Tilføj titlerne til matricen for at gøre output brugervenligt 
    Gradelist_matrix = np.vstack((Titles,Gradelist_order))
    
    #Ændres nu til en pd dataframe for yderligere overskuelighed:
    pd_Gradelist = pd.DataFrame(Gradelist_matrix)
    
    return pd_Gradelist
