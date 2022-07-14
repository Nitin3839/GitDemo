from selenium import webdriver
#driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\msedgedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#from selenium.webdriver.support.ui import Select
#driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
print(driver.title)
driver.find_element_by_name("email").send_keys("mohanlala123@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("patanahi123")
driver.find_element_by_id("exampleCheck1").click()

#//tagname[@atribut='value']  --->  //input[@type='submit']
driver.find_element_by_xpath( "(//input[@type='text']) [3]").send_keys("pathshala")
#msg=driver.find_element_by_class_name("alert-dismissible").text
#print(msg)
driver.find_element_by_xpath( "(//input[@type='text']) [3]").clear()
