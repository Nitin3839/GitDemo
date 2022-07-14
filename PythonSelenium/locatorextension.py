#from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
drop = Select(driver.find_element_by_id("dropdown-class-example"))
#select one option-3 approches
#print(drop.select_by_visible_text('Option2'))
#drop.select_by_value('option2')
#drop.select_by_index(2)

#capture all the option and print that as output
all_option = drop.options
for option in all_option:
    print(option.text)
#cound option
print(len(drop.options))