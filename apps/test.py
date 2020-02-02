# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime as dt

# Set the executable path and initialize the chrome browser in splinter
browser = Browser('chrome', 'chromedriver.exe', headless=False)

# Create list of hemispheres
hemiSearchList = ['Cerberus Hemisphere Enhanced', 'Schiaparelli Hemisphere Enhanced','Syrtis Major Hemisphere Enhanced','Valles Marineris Hemisphere Enhanced']

# Create empty list to store results
hemiList = []

# Cycle through each heimisphere
for item in hemiSearchList:
    
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    # Find and click the full Cerberus image button
    full_image_elem = browser.find_by_text(item)
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    img_url_rel = img_soup.select_one('img.wide-image').get("src")

    # Use the base URL to create an absolute URL
    hemiImg = f'https://astrogeology.usgs.gov{img_url_rel}'

    print(hemiImg)
    
    # # First, the code makes sure an element is present using text. This tells Splinter to search through the HTML
    # # for the specific text "Original" We can verify that it does exist in the HTML by using the DevTools to 
    # # search for it.
    # browser.is_element_present_by_text('Original', wait_time=1)

    # # Create a new variable, to find the link associated with the "Original" text.
    # hemi = browser.links.find_by_partial_text('Original')

    # # Save image link
    # hemiImg = hemi['href']

    # HTML parser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Look for <h2> tag with class title
    hemiTitle = news_soup.select_one('h2.title').text

    # Create dictionary to store Cerberus info
    hemiDic = {'img_url': hemiImg, 'title': hemiTitle}

    # Append dictionary to hemiList
    hemiList.append(hemiDic.copy())

print(hemiList)