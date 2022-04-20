# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:36:23 2021

@author: HTRUJILLO
"""
from scipy.stats.contingency import association
from pandas import DataFrame, crosstab
from numpy import sqrt, zeros, eye
from .pairwise import PairWisemetrics
from itertools import combinations


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
        init a square matrix n x n fill with zeros,
        where n is the total number of categorical variables
        found in the pd.DataFrame

        Returns
        -------
        None.

        '''
        # fill matrix with zeros, except for the main diag (which will
        # be always equal to one)
        self.matrix = DataFrame(
            eye(len(self.cat_columns)),
            columns=self.cat_columns,
            index=self.cat_columns
        )


    def fill_pairwisematrix(self):
        '''
        fills the square matrix using scipy's association method

        Returns
        -------
        None.

        '''
        
        n = len(self.cat_columns)
        # get all possible pair-wise combinations in the columns list
        # this assumes that A-->B equals B-->A so we don't need to
        # calculate the same thing twice
        # we also never get "A --> A"
        all_combinations = combinations(self.cat_columns, r=2)

        # note that because we ignore redundant combinations,
        # we perform half the calculations, so we get the results
        # twice as fast
        for comb in all_combinations:
            i = comb[0]
            j = comb[1]

            # make contingency table
            input_tab = crosstab(self.data[i], self.data[j])

            # find the resulting cramer association value using scipy's
            # association method
            res_cramer = association(input_tab, method='cramer')
            self.matrix[i][j], self.matrix[j][i] = res_cramer, res_cramer


    def fit(self):
        '''
        Creates a pairwise matrix filled with Cramer's V,
        where columns and index are the categorical
        variables of the passed pandas.DataFrame

        Returns
        -------
        Cramer's V matrix.

        '''
        self.select_variables()
        self.init_pairwisematrix()
        self.fill_pairwisematrix()

        return self.matrix
