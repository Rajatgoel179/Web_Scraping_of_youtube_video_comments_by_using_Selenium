from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/watch?v=0iAhG6sQ0no&t=150s")
time.sleep(15)

# Find all comment elements using the correct XPATH
comments = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')

# Scroll to the last comment to ensure all comments are loaded
driver.execute_script("arguments[0].scrollIntoView();", comments[-1])

time.sleep(3)
last_height = driver.execute_script('return document.documentElement.scrollHeight')

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script('return document.documentElement.scrollHeight')

    if new_height == last_height:
        break

    last_height = new_height

# Find all comment elements again after scrolling
comments = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text"]')

for comment in comments:
    print(comment.text)

driver.close()

