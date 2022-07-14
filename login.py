from selenium import webdriver
from selenium.webdriver.support import Select
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import by


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_elements_by_xpath("//input[@type='checkbox']")