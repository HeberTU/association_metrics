# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:30:55 2021

@author: HTRUJILLO
"""
from pandas import DataFrame

class PairWisemetrics:
    
    def __init__(self, dataframe, copy = True):
        '''
        Class initialization, it serves as a base class for all the metrics

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Pandas dataframe containing the variables of interest to measure the degree of association.

        Returns
        -------
        None.

        '''
        if isinstance(dataframe, DataFrame):
        
            if copy:
                self.data = dataframe.copy()
            else:
                self.data = dataframe
                
        else:
            raise TypeError("dataframe must be an instance of a pandas.DataFrame")

    def measure_association(self):
        pass