# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:32:11 2021

@author: HTRUJILLO
"""
import unittest
import association_metrics as am
from pandas import DataFrame, read_csv


class TestMetrics(unittest.TestCase):
    
    
    
    
    def test_pairwisemetrics(self):
        
        dataframe = DataFrame(
            data = {
                'A_Var': [1,2,3,4,5],
                'B_Var': [6,7,8,9,10]})
        
        pairwisemetrics = am.PairWisemetrics(dataframe)
        self.assertIsInstance(pairwisemetrics.data, DataFrame)
        
    def test_camers_select_variables(self):
        tips = read_csv(
            "./association_metrics/datasets/tips.csv")
        tips = tips.apply(
            lambda x: x.astype("category") if x.dtype == "O" else x)
    
        cramersv = am.CramersV(tips)
        cramersv.select_variables()
        cat_columns = list(cramersv.cat_columns)
        tips_cat_names = ["sex", "smoker", "day", "time"]
        self.assertEqual(cat_columns, tips_cat_names)
        
    def test_cramers_init_pwmatrix(self):
        tips = read_csv(
            "./association_metrics/datasets/tips.csv")
        tips = tips.apply(
            lambda x: x.astype("category") if x.dtype == "O" else x)
    
        cramersv = am.CramersV(tips)
        cramersv.select_variables()
        cramersv.init_pairwisematrix()
        matrix_shape = cramersv.matrix.shape
        self.assertEqual(matrix_shape, (4,4))
        
    def test_cramers_fit(self):
        tips = read_csv(
            "./association_metrics/datasets/tips.csv")
        tips = tips.apply(
            lambda x: x.astype("category") if x.dtype == "O" else x)
        cramersv = am.CramersV(tips)
        matrix = cramersv.fit()
        contratype = DataFrame(
            data = {
                "sex": [1.000000, 0.002816, 0.232784, 0.205231],
                "smoker": [0.002816, 1.000000, 0.325093, 0.054921],
                "day": [0.232784, 0.325093, 1.000000, 0.943295],
                "time": [0.205231, 0.054921, 0.943295, 1.000000]},
            index = ["sex", "smoker", "day", "time"])
        total_cramersv = round(matrix.sum().sum(),5)
        total_contratype = round(contratype.sum().sum(),5)
        self.assertEqual(total_cramersv,total_contratype)
        
if __name__ == '__main__':
    
    unittest.main()
