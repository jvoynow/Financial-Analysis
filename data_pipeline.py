# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:45:07 2020

@author: voyno
"""

import pandas as pd

# import preprocessing, fill_nan scripts
from preprocessing import preprocess
from fill_nans import fill_nans


def run_pipeline(file):

    # Read raw data from yfinance api
    df = pd.read_csv(file)

    # preprocessing on raw data
    df = preprocess(df)

    # removing nan values
    df = fill_nans(df)

    # now data is prepared to model
    return df
