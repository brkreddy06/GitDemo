from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

# Checkboxes
#to tick all the checkboxes use for loop
#for checkbox in checkboxes:
   # checkbox.click()
   # assert checkbox.is_selected()

#to tick specific checkbox then use get_attribute() method in if condition with in for loop
for checkbox in checkboxes:
    print(checkbox.get_attribute('value'))  #value attribute has specific text for each checkbox thats why we considered value
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()

# Radio buttons
radiobutton = driver.find_elements_by_xpath("//input[@type='radio']")
print(len(radiobutton))
#print(radiobutton[1:3])
radiobutton[2].click()
assert radiobutton[2].is_selected()

# is_displayed() - it returns true or false
print(driver.find_element_by_css_selector("#displayed-text").is_displayed())

assert driver.find_element_by_css_selector("#displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_css_selector("#displayed-text").is_displayed())

assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()