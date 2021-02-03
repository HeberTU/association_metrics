# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:36:23 2021

@author: HTRUJILLO
"""
from scipy.stats import chi2_contingency
from pandas import DataFrame,crosstab
from numpy import sqrt, zeros
from pairwise import PairWisemetrics

class CramersV(PairWisemetrics):
    
    def __init__(self):
        PairWisemetrics.__init__(self)
        
    
    def measure_association():
        pass