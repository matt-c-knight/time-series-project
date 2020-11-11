import pandas as pd
import numpy as np
import acquire
from acquire import get_codeup_data



def prep_codeup_data(df):
    df.columns = ['date', 'time', 'page_viewed', 'user_id', 'cohort_id', 'ip']
    df.dropna(inplace=True)


def prep_cohort_data(df):
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df[['cohort_id', 'name', 'start_date', 'end_date']]
