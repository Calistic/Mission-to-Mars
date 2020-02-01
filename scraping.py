# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
browser = Browser('chrome', 'chromedriver.exe', headless=False)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# HTML parser
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

# Look for <ul /> and <li /> tags with classes item_list and slide
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Scrape news titles
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that

# First, the code makes sure an element is present using text. This tells Splinter to search through the HTML
# for the specific text "more info." We can verify that it does exist in the HTML by using the DevTools to 
# search for it. We also add a wait time of one second to make sure that everything in the page is finished 
# loading before we search for it.
browser.is_element_present_by_text('more info', wait_time=1)

# Next, we create a new variable, more_info_elem, to find the link associated with the "more info" text.
more_info_elem = browser.find_link_by_partial_text('more info')

# Finally, we tell Splinter to click that link by chaining the .click() function onto our more_info_elem variable.
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find the relative image url

# The <figure /> and <a /> tags have the image link nested within them.

# figure.lede references the <figure /> tag and its class, lede
# a is the next tag nested inside the <figure /> tag. Then <img />
# .get("src") pulls the link to the image.
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Space Facts Table

# the [0] tells pandas to only pull the first table it sees
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']

# inplace=True means that the updated index will remain in place, without having to reassign the
# DataFrame to a new variable
df.set_index('description', inplace=True)
df

# converto df to html
df.to_html()

# close browswer
browser.quit() 
