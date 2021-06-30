# Webscraper Tutorial
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
# selenium is a web-based automation tool used for testing and webscraping
# webdriver allows selenium to execute cross-browser tests
# common keys is used to ID different keys on the keyboard

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# selects the path to find the chrome browser to use

driver.get("https://www.techwithtim.net/")
print(driver.title)
# selects what website to look at and provides the site title

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()
# this tells the programme to wait 10 seconds until the an item is located
# on the page before it continues to move on to the next part of the script
