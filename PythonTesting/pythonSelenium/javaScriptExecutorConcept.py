#JavaScript DOM can access any elements on web page just like how selenium does.
# Selenium have a method to execute javascript code in it.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Ram")
print(driver.find_element_by_name("name").text) # what ever we printed on the text box won't display
print(driver.find_element_by_name("name").get_attribute('value'))  # this get_attribute method will get the value entered by the user
print(driver.execute_script('return document.getElementsByName("name")[0].value')) # this is purely javascript

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)  # shopButton variable will store in the arguments with index value

driver.execute_script("window.scroll(0,document.body.scrollHeight);")  # it will scroll the webpage till bottom


