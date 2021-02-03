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
    
    def __init__(self, dataframe):
        PairWisemetrics.__init__(self, dataframe)
        self.matrix = None
        
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
        self.matrix = DataFrame(
            data = zeros(
                (len(self.cat_columns),len(self.cat_columns))),
        columns = self.cat_columns,
        index = self.cat_columns)
        
     
    def measure_association(self, x, y):
        '''
        Calculates Cramer's V based on Pearson's chi-squared statistic
        
        Parameters
        ----------
        x : pandas.Series containing one categorical variable
        
        y : pandas.Series containing one categorical variable
        
        Returns
        -------
        v: float 
        cramers value

        '''
        if x.nunique()== 1 or y.nunique()== 1:
            x_name = x.name
            y_name = y.name
            msg = "{} and {} ".format(x_name, y_name)
            msg += "must have at least 2 different levels"
            raise ValueError(msg)
        
        contingency_table = crosstab(x,y)
        chi2 = chi2_contingency(contingency_table, correction = False)[0]
        
        n = contingency_table.sum().sum()
        mindim = min(contingency_table.shape)-1
        
        v = sqrt((chi2/n)/mindim)
    
        return v
        
    def fill_pairwisematrix(self):
        '''
        fills the square matrix using measure_association method

        Returns
        -------
        None.

        '''
        
        n = len(self.cat_columns)
        
        for i in range(0,n):
            x = self.cat_columns[i]
            for j in range(i,n):
                y = self.cat_columns[j]
                
                if x == y:
                    self.matrix[x][y] = 1
                else:
                    value = self.measure_association(
                        self.data[x], self.data[y])
                    self.matrix[x][y] = value
                    self.matrix[y][x] = value
    
    def fit(self):
        '''
        Creates a pairwise matrix filled with Cramer's V, where columns and index are the categorical variables of the passed pandas.DataFrame

        Returns
        -------
        Cramer's V matrix.

        '''
        self.select_variables()
        self.init_pairwisematrix()
        self.fill_pairwisematrix()
        
        return self.matrix