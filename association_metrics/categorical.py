# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:36:23 2021

@author: HTRUJILLO
"""
from scipy.stats import chi2_contingency
from pandas import DataFrame,crosstab
from numpy import sqrt, zeros
from .pairwise import PairWisemetrics

class CramersV(PairWisemetrics):
    
    def __init__(self):
        PairWisemetrics.__init__(self)
        
    def select_variables(self):
        '''
        Selects all category variables

        Returns
        -------
        None.

        '''
        self.cat_columns = self.data.select_dtypes(
            include=['category']).columns
        
        if len(self.cat_columns)==0:
            raise KeyError("No categorical variables found")
    
    def init_pairwisematrix(self):
        '''
        init a square matrix n x n fill with zeros, where n is the total number of categorical variables found in the pandas.DataFrame

        Returns
        -------
        None.

        '''
        self.matriz_cramer = DataFrame(
            data = zeros(
                (len(self.cat_columns),len(self.cat_columns))),
        columns = self.cat_columns,
        index = self.cat_columns)
        
     
    def measure_association(self):
        '''
        Calculates Cramer's V based on Pearson's chi-squared statistic

        Returns
        -------
        None.

        '''
        pass