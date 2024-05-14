from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

def open_wikipedia(url):
    # Create a Chrome driver instance
    driver = webdriver.Chrome()

    # Set implicit wait time
    driver.implicitly_wait(10)

    # Open the provided URL
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))

    time.sleep(600)
    # Close the browser window
    driver.quit()

def open_youtube(url):
    # Create a Chrome driver instance
    driver = webdriver.Chrome()

    # Set implicit wait time
    driver.implicitly_wait(10)

    # Open the provided URL
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "searchInput")))

    time.sleep(600)
    # Close the browser window
    driver.quit()