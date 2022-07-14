import time

from selenium import webdriver
#from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item']")
for country in countries:
    if country.text == "India":
        country.click()
        break