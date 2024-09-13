import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from url_grabber import url_grabber
from post_scraper import multi_post_scraper
from data_format import format_data, clean_date,process_text
from data_format import parallelize_dataframe,apply_language_detection

#params
BASEURL = "https://www.finansavisen.no/forum/" #The forum URL
PAGELIMIT = 1 #can increase
POSTLIMIT = 1 #can increase

urldata,titledata,tickerdata = url_grabber(BASEURL,PAGELIMIT)
contentdata,userdata = multi_post_scraper(POSTLIMIT,urldata)

df = format_data(contentdata,userdata)

df["Timestamp"] = clean_date(df["Timestamp"])
df["Value"] = pd.to_numeric(df["Value"],downcast="integer")
df["Content"] = process_text(df["Content"])
df = df.dropna()

#parallel processing to the DataFrame
df = parallelize_dataframe(df, apply_language_detection, n_cores=11)  #adjust n_cores based on your CPU
df = df[df["Language"] == "no"]

# pd.DataFrame.to_csv(df,"OUTPUT_PATH", index=False)

engine = create_engine("postgresql+psycopg2://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME")

df.to_sql(name="NAME_OF_TABLE", schema="NAME_OF_SCHEMA", con = engine, if_exists="append")
print("Completed ",len(df))