# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Google Maps
driver.get("https://www.google.com/maps")
time.sleep(5)

# Finding the search bar and entering the address
search_bar = driver.find_element("id","searchboxinput")
search_bar.send_keys("100 Jamieson Pkwy, Cambridge, ON, CA")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)


# Selecting a laptop from the search results
search_bar = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span")
search_bar.click()
time.sleep(5)

# Entering the starting point

search_bar_2 = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
search_bar_2.send_keys("75 Pinebush road, Cambridge, ON, CA")
search_bar_2.send_keys(Keys.RETURN)
time.sleep(5)


# CLicking the reverse button to swap the starting and the ending points
reverse_link = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[2]/button/span")
reverse_link.click()
time.sleep(5)



# Choosing Cycling method
cycling_link = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[5]/button")
cycling_link.click()
time.sleep(5)

# Adding one more destination
destintion_link = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/button/div[1]/div/span")
destintion_link.click()
time.sleep(5)

# Entering the third destination
#search_bar_3 = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div[1]/div/input")
search_bar_3 = driver.find_element("xpath","/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div[2]")



driver.close()
