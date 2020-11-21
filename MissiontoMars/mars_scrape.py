from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

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
    "Latest Title": latest_title,
    "Latest Para" : latest_para
    }

    browser.quit()

    return mars_data