# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:32:11 2021

@author: HTRUJILLO
"""
import unittest
import association_metrics as am
from pandas import DataFrame


class TestMetrics(unittest.TestCase):
    
    def test_pairwisemetrics(self):
        
        dataframe = DataFrame(
            data = {
                'A_Var': [1,2,3,4,5],
                'B_Var': [6,7,8,9,10]})
        
        pairwisemetrics = am.PairWisemetrics(dataframe)
        self.assertIsInstance(pairwisemetrics.data, DataFrame)
        
        
if __name__ == '__main__':
    unittest.main()