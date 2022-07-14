from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
print(driver.title)
#driver.find_elements_by_xpath("//a[contains(@href,'shop')]").click()
#driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
#driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products= driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()
success_msg = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
print(success_msg)
assert "Success! Thank you! " in success_msg
driver.close()