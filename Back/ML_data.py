import pandas as pd
import numpy as np


class ML_data:
    """Data structure for Machine Learning algorithms"""
    def __init__(self):
        self.pd_data = None
        self.target = None
        self.feature = None
        self.ml = None
        self.target_type = None
        self.feature_type = None

    def set_pd_data(self,data):
        self.pd_data = data

    def set_target(self, data):
        self.target = self.pd_data[data].to_numpy().ravel()
        self.target_type = self.pd_data[data].dtypes

    def set_features(self,data):
        self.feature = self.pd_data[data]
        self.feature = self.feature.to_numpy()
        self.feature_type = self.pd_data[data].dtypes
