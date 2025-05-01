import sqlite3                    # Chosen SQL database
from datetime import datetime, timezone, timedelta    # Helps us convert the UNIX time into legible format and vice-versa
import time                       #Allows us to have the now() method
import pandas as pd

def calculate_sma(df, window):
    """Calculates SMA (Simple Mean Average) within a certain window of time and returns a Series"""
    return df.rolling(window=window).mean()

def calculate_atr(df, period):
    """
    Calculates Average True Range (ATR) with a DataFrame with OHLC data for a given time period.

    Args:
        df (pd.DataFrame): a DataFrame with 'High', 'Low' and 'Close'
        period (int): period to calculate ATR
    """
    high = df['high']
    low = df['low']
    previous_close = df['close'].shift(1)

    tr1 = high - low
    tr2 = abs(high - previous_close)
    tr3 = abs(low - previous_close)
    tr = pd.concat([tr1, tr2, tr3], axis = 1).max(axis=1)

    atr = tr.rolling(window=period).mean()
    
    return atr

def calculate_bollinger_bands(df, win, num_std=2):
    """Calculates Bollinger Bands
    Args:
    df (pd.DataFrame): a DataFrame with 'High', 'Low' and 'Close',
    win (int): window of time
    num_sdt (int): standard deviation fixed variable"""

    sma = df.rolling(window=win).mean()
    std = df.rolling(window=win).std()
    upper_band = sma + (num_std * std)
    lower_band = sma - (num_std * std)
    return upper_band, lower_band

def calculate_returns_std(df, win):
    returns = df.pct_change() 
    return (returns.rolling(window=win).std()) * 100