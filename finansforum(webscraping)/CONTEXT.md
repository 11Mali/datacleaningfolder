
# Finance forum data extraction

**keywords: Webscraping, Data cleaning, Data transformation, Data storage**

This project is a Python-based web scraper and data processor designed to collect and process forum data from financial discussion boards, specifically Finansavisen. It scrapes forum posts, user data, and stock ticker information, processes the content by cleaning and transforming the data, and stores it in a PostgreSQL database.

**This script is apart of a larger sentiment analysis script using word embedding and clustering.**\
*Can be found here* - "oops not ready yet :("

### Features
**Web Scraping** - Extracts forum post content, user data, and stock tickers.\
**Data Cleaning** - Cleans the scraped data for further analysis (e.g., date formatting, text cleaning, handling missing values).\
**Language Detection** - Applies parallelized language detection to filter content based on the Norwegian language.\
**Data Storage** - Stores processed data in a PostgreSQL database.


**Prerequisites**
- Python 3.11
- PostgreSQL Database

*Required Python libraries:*
- psycopg2
- pandas
- sqlalchemy
- requests
- beautifulsoup4
- langdetect
- multiprocessing


### Usage

You can run this by setting up the environment and configuring your PostgreSQL connection details. Here’s how:

Set the BASEURL, PAGELIMIT, and POSTLIMIT.
Adjust the database connection details (USERNAME, PASSWORD, etc.).
Execute the script to scrape, clean, and store data in the database:

Using python webscraping_main.py