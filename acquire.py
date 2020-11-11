import numpy as np
import pandas as pd
import os

def new_codeup_data():
    df = pd.read_csv('curriculum.txt',
                engine='python',
                 header=None,
                 index_col=False,
                 sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                 na_values='"-"',)
    return df

def get_codeup_data(cached=False):
    if cached or os.path.isfile('curriculum.txt') == False:
        df = new_codeup_data()
    else:
        df = pd.read_csv('curriculum.txt',
                engine='python',
                 header=None,
                 index_col=False,
                 sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                 na_values='"-"',)
    return df

def new_cohort_data():
    cohort = pd.read_csv('cohort_name.csv')
    return cohort

def get_cohort_data(cached=False):
    if cached or os.path.isfile('cohort_name.csv') == False:
        df = new_cohort_data()
    else:
        df = pd.read_csv('cohort_name.csv')
                
    return df
