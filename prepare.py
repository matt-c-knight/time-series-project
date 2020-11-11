import pandas as pd
import numpy as np
import acquire
from acquire import get_codeup_data



def prep_codeup_data(df,df2):
    df.columns = ['date', 'time', 'page_viewed', 'user_id', 'cohort_id', 'ip']
    df.dropna(inplace=True)
    df = pd.merge(df, df2, on='cohort_id')
    df.cohort_id = df.cohort_id.astype('int')
    df['date'] = df.date + " " + df.time
    df.drop(columns=('time'), inplace=True)
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date')
    return df

def prep_cohort_data(df):
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df[['cohort_id', 'name', 'start_date', 'end_date']]
    df.cohort_id = df.cohort_id.astype('int')
    return df