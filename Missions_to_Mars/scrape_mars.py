from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    ## JPL Mars Space Images—Featured Image
    img_url="https://spaceimages-mars.com"
    browser.visit(img_url)
    xpath='/html/body/div[1]/div/a'
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url=img_url+"/"+image_url
# ### Mars Facts
    facts_url="https://galaxyfacts-mars.com"
    browser.visit(facts_url)
    time.sleep(1)
    tables = pd.read_html(facts_url)
    tables
    df = tables[0]
    df
    html_table = df.to_html()
    html_table.replace('\n', '')
# ### Mars Hemispheres
    mars_url="https://marshemispheres.com/"
    browser.visit(mars_url)
    time.sleep(1)
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain item
    items = soup.find_all('div', class_='item')
    hemisphere_img_urls=[]
    # Iterate through each item
    for item in items:
        title = item.find('h3').text
       
    
#     find the itemlink:<a href="cerberus.html" class="itemLink product-item">
        hemi_url=mars_url+item.find("a",class_="itemLink product-item")["href"]
        browser.visit(hemi_url)
        html = browser.html
        time.sleep(1)
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find("img", class_="wide-image")["src"]
        hemi_img_url=mars_url+img_url
        hemisphere_img_urls.append({'title': title, 'img_url':hemi_img_url})

#Append the dictionary with the image URL string and the hemisphere title to a list. 
#This list will contain one dictionary for each hemisphere.
    
    browser.quit()

    # Return our dictionary
        # Mars 
    mars_dict = {
        "news_title": news_title,
        
        
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(html_table),
        "hemisphere_images": hemisphere_img_urls
    }

    return mars_dict     



