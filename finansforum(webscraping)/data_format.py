import pandas as pd
import numpy as np
import re

from datetime import date, timedelta

from langdetect import detect
from multiprocessing import Pool


"""
Format the data recieved from scraping
Datatransform the data recieved from formating

"""

def format_data(contentdata,userdata):
    #current date
    current_date = date.today().strftime("%d-%m-%y")

    #split each row by semicolon
    list = [row.split(';') for row in userdata]
    #adjust rows where stock information is missing and elements are shifted
    for i, row in enumerate(list):
        if len(row) == 3:  #when there are 3 elements instead of 4 (no stock value)
            list[i] = [row[0], None, row[1], row[2]]  #shift elements to the correct columns

    #create df
    user_df = pd.DataFrame(list, columns=['User', 'Ticker', 'Timestamp', 'Value'])
    #fill missing Ticker values with the previous valid value
    user_df['Ticker'] = user_df['Ticker'].ffill()

    #df for contentdata
    content_df = pd.DataFrame(contentdata,columns=["Content"])
    df = pd.concat([content_df,user_df], axis=1)

    #drop duplicates and missing value rows
    df["Content"] = df["Content"].drop_duplicates()
    df = df.dropna()

    return df


def clean_date(column):
    current_date = date.today().strftime("%d.%m.%Y")
    yester_date = (date.today() - timedelta(1)).strftime("%d.%m.%Y")
    column = column.str.replace(r"(?i)^I dag", current_date, regex=True)  #replace "I dag" with today's date
    column = column.str.replace(r"(?i)^I går", yester_date, regex=True)   #replace "I går" with yesterday's date
    column = column.str.replace("kl","") #str
    column = column.str.replace(r"\D", "", regex=True)
    return pd.to_datetime(column, format ="%d%m%Y%H%M")

def clean_text(text):
    #the value is treated as a string
    text = str(text)
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text, flags=re.MULTILINE) #links
    text = re.sub(r"[^A-Za-z0-9øæå]+", " ", text)#include norwegian letters
    text = text.lower()
    return text

def process_text(column): #a quick preliminary clean
    column = column.apply(clean_text)
    return column


""""
Language detection through parallelized dataframe

"""

#define a function to detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return "Error"  #return an error tag in case of failure

#split data and apply function in parallel
def parallelize_dataframe(df, func, n_cores=11):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

#applies the language detection
def apply_language_detection(df):
    df["Language"] = df["Content"].apply(detect_language)
    return df
