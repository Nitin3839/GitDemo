from selenium import webdriver
from selenium.webdriver.chrome.service import service
driver = webdriver.Chrome("C:\chromedriver.exe")

chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("headless")
#chrom_options.add_argument("--ignore-certificate-errors")

service_options = service("https://rahulshettyacademy.com/AutomationPractice/")
driver.get(service = service_options, option = chrom_options)
driver.implicitly_wait(2) #10sec
#assert "Practice Page" in driver.title
#driver.find_element_by_id("name").send_keys("nitin")
#driver.find_element_by_id("alertbtn").click()
#alt = driver.switch_to.alert
#print(alt.text)
#alt.accept()
#alt.dismiss()

#driver.execute_script("window.scrollBy(0,2000)")
#driver.get_screenshot_as_file("scree.pnj")
