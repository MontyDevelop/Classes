from selenium import webdriver


# driver = webdriver.Edge()

# --------------------------------------------
# automatic Task 1:
# opening the website

# driver.get("https://www.python.org")

# print(driver.title)
# ---------------------------------------------


# Automation Task 2:
# Lets make python open browser and make a search query

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME,"q")

search_box.send_keys("Arduino projects")

search_box.send_keys(Keys.ENTER)

input("Press Enter to close the browser")

driver.quit()