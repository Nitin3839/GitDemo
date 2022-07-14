from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_css_selector("input[minlength='2']").send_keys("zamala")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
