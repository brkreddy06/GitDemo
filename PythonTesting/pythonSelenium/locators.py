#Select class provide the methods to handle the options in dropdown

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Ramkumar")
#driver.find_element_by_name("email").send_keys("abcd@abc.com")
driver.find_element_by_css_selector("input[name='email']").send_keys("1123@123.com")  # css
driver.find_element_by_id("exampleInputPassword1").send_keys("Welcome123")
driver.find_element_by_id("exampleCheck1").click()

#Select class.  pass the locator as an argument in to the select class then only the select class will identify the dropdown
dropdown = Select(driver.find_element_by_css_selector("#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")  # its select the option which is visible
dropdown.select_by_index(0)  # its select the value based on index value, in this ex Male - 0, Female - 1 index
#dropdown.select_by_value("M")  # its select the option in the dropdown based on the value present in html code ex: <option value="M">Male</option>


#driver.find_element_by_id("exampleFormControlSelect1").is_selected("Female")
driver.find_element_by_xpath("//Input[@type='submit']").click()   # xpath

#print(driver.find_element_by_class_name("alert-success").text) # class name
#print(driver.find_element_by_css_selector("div[class*='alert-success']").text)  # * is a regular expression which is used to get the match of the text/class present in the class attribute
#print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text) # either can use * or tagname

#div[class*='alert-success'] - CSS
#//div[contains(@class,'alert-success')] - Xpath

# To check the alert message is present or not - use assert method
message = driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text

#assert 'submitted' in message  # to check substring or partial message use keyword 'in'
assert message == message  # to check exact msg use == keyword

