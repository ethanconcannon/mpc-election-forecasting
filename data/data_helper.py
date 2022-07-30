from typing import Optional
import pandas as pd
from datetime import datetime as dt

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # get rid of polls that are not for the general election
    df = df.drop(df[df['stage'] != 'general'].index)
    
    # get rid of polls that are not for the 2022 election
    df = df.drop(df[df['cycle'] != 2022])
    
    bad_cols: list[str] = ['pollster', 'sponsor_ids', 'sponsors', 'display_name', 'pollster_rating_name', 
                           'methodology','sponsor_candidate', 'sponsor_candidate_party', 'subpopulation', 
                           'population_full', 'tracking', 'notes', 'url', 'source', 'internal', 'partisan', 
                           'cycle', 'stage', 'ranked_choice_reallocated']
    df = df.drop(columns=bad_cols)
    return df

def data_between_start_and_end(df: pd.DataFrame, start: Optional[dt.datetime]=None, 
                               end: Optional[dt.datetime]=None) -> pd.DataFrame:
    if start is not None:
        df = df[df['end_date'] >= start]
    if end is not None:
        df = df[df['end_date'] <= end]
    return df

def get_senate_polls_current() -> pd.DataFrame:
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/data/senate_polls.csv')
    return df

def get_senate_polls_historical() -> pd.DataFrame:
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/data/senate_polls_historical.csv')
    return df

def get_house_polls_current() -> pd.DataFrame:
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/data/house_polls.csv')
    return df

def get_house_polls_historical() -> pd.DataFrame:
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/data/house_polls_historical.csv')
    return df