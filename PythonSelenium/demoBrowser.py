from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_name("name").send_keys("AMAN KHAN")
driver.find_element_by_name("email").send_keys("AMAN KHAN@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("123456")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_id("exampleFormControlSelect1").send_keys("female")
