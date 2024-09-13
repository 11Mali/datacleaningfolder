import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import threading
import time


"""
scrapes through the pages of a single post
after getting the input of how many https forum post are to be scraped

returns contentdata, userdata

"""

def multi_post_scraper(POSTLIMIT, urldata):
    start_time = time.time()
    contentdata = []
    userdata = []
    
    #lock to prevent race conditions when appending to lists
    data_lock = threading.Lock()

    def scrape_page(url, page):
        page_url = f"{url}?page={str(page)}"
        print(f"Scraping URL: {page_url}")
        
        try:
            response = requests.get(page_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return
        
        forum = BeautifulSoup(response.content, "lxml")

        #extract contents
        contents = forum.find_all('div', class_="post content text-left")
        print(f"Found {len(contents)} contents on page {page}")

        with data_lock:
            for content in contents:
                postdata = content.get_text(strip=True)
                contentdata.append(postdata)

        print(f"Finished extracting data on {len(contents)} contents on page {page}")

        #extract user data
        users = forum.find_all('div', class_="d-flex flex-column flex-md-row align-items-md-center")
        print(f"Found {len(users)} users on page {page}")

        with data_lock:
            for user in users:
                metadata = user.get_text(strip=True, separator=";")
                userdata.append(metadata)

        print(f"Finished collecting data on {len(users)} users on page {page}")

    threads = []
    
    for url in urldata:
        for page in range(1, POSTLIMIT + 1):
            #create a thread for each page
            thread = threading.Thread(target=scrape_page, args=(url, page))
            threads.append(thread)
            thread.start()
            time.sleep(0.1)  #short delay to avoid overwhelming the server
            #mind you they ask for 10s delay, 0.1 is due to testing
    
    #wait for all threads to complete
    for thread in threads:
        thread.join()

    print("--- %s seconds ---" % round((time.time() - start_time), 2))
    return contentdata, userdata
