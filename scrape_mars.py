from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    scrape = {}
    
    # NASA Mars News
    browser = init_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    li = soup.find('li', class_='slide')
    div = li.find("div", class_="content_title")
    news_title = div.find("a").get_text()
    news_p = soup.find("div", class_="article_teaser_body").get_text()
    scrape["headline"] = news_title
    scrape["text"] = news_p
    browser.quit()

    # Featured image
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    li = soup.find('li', class_='slide')
    a = li.find('a')
    href = a['data-fancybox-href']
    featured_img_url = 'https://www.jpl.nasa.gov' + href
    alt = a['data-description']
    scrape["src"] = featured_img_url
    scrape["alt"] = alt
    browser.quit()

    # Mars Facts table
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    html_table=df.to_html()
    scrape["html"] = html_table

    # Mars Hemispheres
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('Cerberus')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='downloads')
    a = div.find('a')
    href = a['href']
    h2 = soup.find('h2', class_='title').get_text()
    scrape["src2"] = href
    scrape["alt2"] = h2
    scrape["title2"] = h2
    browser.quit()

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('Schiaparelli')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='downloads')
    a = div.find('a')
    href = a['href']
    h2 = soup.find('h2', class_='title').get_text()
    scrape["src3"] = href
    scrape["alt3"] = h2
    scrape["title3"] = h2
    browser.quit()
    
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('Syrtis')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='downloads')
    a = div.find('a')
    href = a['href']
    h2 = soup.find('h2', class_='title').get_text()
    scrape["src4"] = href
    scrape["alt4"] = h2
    scrape["title4"] = h2
    browser.quit()
    
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    browser.click_link_by_partial_text('Valles')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='downloads')
    a = div.find('a')
    href = a['href']
    h2 = soup.find('h2', class_='title').get_text()
    scrape["src5"] = href
    scrape["alt5"] = h2
    scrape["title5"] = h2
    browser.quit()
    
    
    
    
    
    return scrape