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
# selects what website to look at

link = driver.find_element_by_link_text("Python Programming")
link.click()
# finds and clicks the link "python programming"

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
# finds the element link text and clicks it


    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()
# finds the id of another link and clicks that

    driver.back()
    driver.back()
    driver.back()
    # goes back to the previous page



except:
    driver.quit()