


import json, time
from sys import argv

import bs4
from tqdm import tqdm

from utils import save_obj

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
This parameter has been changed in the past. Check Google images result page source code if this doesn't work.
"""

html_string = "div[class='rg_meta notranslate']"

""" 
Function to create headless webdriver
"""
def init_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)
    driver.wait = WebDriverWait(driver, 5)
    return driver

""" 
Google images lookup
"""

def lookup(driver, query):
    driver.get('https://www.google.ie/imghp')
    try:
        box = driver.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnG")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print('Box or button not found on Google Images')
        
"""
Uses BeautifulSoup to parse the urls of images
"""

def urls_list(driver, string):
    src = driver.page_source
    soup = bs4.BeautifulSoup(src, 'html.parser')
    raw = soup.select(string)
    urls = [json.loads(row.contents[0])['ou'] for row in raw]
    if len(urls) == 0:
        print("Need to change html_string parameter in google_images_scraper.py")
    return urls

"""
Uses the other functions to return a list of urls
"""

def url_extractor(animal):
    query = animal + ' flag'
    driver = init_driver()
    lookup(driver, query)
    time.sleep(1)
    urls = urls_list(driver, html_string)
    driver.quit()
    return urls

def scraper(file):
    with open(file) as f:
        lst = f.read().splitlines()

    urls_of_imgs = {}

    for i in tqdm(lst):
        urls_of_imgs[i] = url_extractor(i)

    save_obj(urls_of_imgs, file[:-4] + '_dict')

if __name__ == "__main__":
    scraper(argv[1])
