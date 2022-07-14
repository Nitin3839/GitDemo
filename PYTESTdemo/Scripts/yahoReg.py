from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://login.yahoo.com/account/create?.intl=us&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com")
print(driver.title)

driver.find_element(By.CSS_SELECTOR, "#usernamereg-firstName").send_keys('nitin')
driver.find_element(By.XPATH, "//input[@id='usernamereg-lastName']").send_keys("sen")
driver.find_element(By.XPATH, "//input[@id='usernamereg-userId']").send_keys('nitinsen782')
driver.find_element(By.XPATH, "//input[@id='usernamereg-password']").send_keys("MBAchaiwala@12345")
driver.find_element(By.XPATH, "//input[@id='usernamereg-birthYear']").send_keys("1991")
#CHECK TERMS
#driver.find_element(By.CSS_SELECTOR, "a[class='termsLink']").click()
driver.find_element(By.CSS_SELECTOR, "#reg-submit-button").click()
drop= select(driver.find_element(By.NAME, "shortCountryCode"))
drop.select_by_visible_text("India (+91)")
number= driver.find_element(By.CSS_SELECTOR, " #usernamereg-phone ").send_keys("7328834646")

driver.find_element(By.CSS_SELECTOR, "#reg-submit-button").click()
