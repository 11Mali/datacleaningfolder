import requests
from requests.exceptions import RequestException

from bs4 import BeautifulSoup

import time

"""
function that extracts the https for x amount of pages
returns urldata,titledata,tickerdata

"""

def url_grabber(BASEURL,PAGELIMIT):
    start_time = time.time()
    #Creating lists to test if it worked correctly
    urldata = []
    titledata = []
    tickerdata = []

    for page in range(1, PAGELIMIT + 1):
        url = f"{BASEURL}?page={str(page)}"
        print(f"Scraping URL: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            break

        #forum
        forum = BeautifulSoup(response.content, "lxml")
        
        #now i have to extract only the main threads on the forum
        threads = forum.find_all("a", class_="thread pr-2")
        tickers = forum.find_all("td",class_="thread-ticker text-left")

        #loop to get all hrefs on forum page
        for href in threads:
            href= href.get("href")
            urldata.append(href)

        for ticker in tickers:
            ticker = ticker.get_text(strip=True)
            tickerdata.append(ticker)

        for title in threads:
            title = title.get_text(strip=True)
            titledata.append(title)
        
        print(f"Found {len(urldata)} hrefs")
        print(f"Found {len(tickerdata)} tickers")
        print(f"Found {len(titledata)} titles")

        #pause
        time.sleep(1)
        
    print("--- %s seconds ---" % round((time.time() - start_time),2))
    return urldata,titledata,tickerdata
