from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def mars_scrape():

    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    all_news_title = soup.find_all("div", class_="content_title")
    latest_title = news_title[1].find("a").get_text()

    all_news_para = soup.find_all("div", class_="article_teaser_body")
    latest_para = all_news_para[0].get_text()

    mars_data = {
    "latest_title": latest_title,
    "latest_para" : latest_para,
    "html_table": html_table,
    "image_scrape": image_scrape,
    "hemi_scrape": hemi_scrape
    }

    browser.quit()

    return mars_data

def table_scrape():

    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)
    mars_table = tables[0]

    mars_table.columns = ["Description", "Mars"]
    mars_table = mars_table.set_index("Description")

    html_table = mars_table.to_html()
    html_table = html_table.replace('\n', '')

    html_table = {
        "html_table": html_table
        } ############{{ myvariable|safe }}###########

    return html_table

def featured_image_scrape():

    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    browser.find_by_id('full_image').click()

    browser.find_by_text("more info     ").click()

    html = browser.html
    soup = bs(html, "html.parser")

    url = soup.find("img", class_="main_image")["src"]
    image_url = "https://www.jpl.nasa.gov" + url

    browser.quit()

    image_scrape = {
        "featured_image": image_url
    }

    return image_scrape

def hemi_scrape():

    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    hemi_scrape = []

    for i in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
    
        title = soup.find_all("h3")[i].get_text()
        browser.find_by_tag('h3')[i].click()
    
        html = browser.html
        soup = bs(html, "html.parser")
    
        image_url = soup.find("a", text="Sample")["href"]
    
        hemi_scrape.append({
            "title": title,
            "image_url": image_url
        })
        browser.back()

    browser.quit()

    return hemi_scrape