from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
validateText = "Ram"

#Alert with OK button
driver.find_element_by_id("name").send_keys(validateText)
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)   # it will print the alert message
alertText = alert.text
assert validateText in alertText
alert.accept() # click ok button on the alert popup

#Confirm with OK & Cancel button
driver.find_element_by_id("name").send_keys(validateText)
driver.find_element_by_css_selector("#confirmbtn").click()
confirmation = driver.switch_to.alert
print(confirmation.text)
confirmText = confirmation.text
assert validateText in confirmText
confirmation.dismiss() # to click cancel