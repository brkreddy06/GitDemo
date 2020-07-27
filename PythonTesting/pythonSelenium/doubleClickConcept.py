from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://www.chercher.tech/practice/practice-pop-ups-selenium-webdriver")

doubleClick = driver.find_element_by_xpath("//input[@id='double-click']")
action = ActionChains(driver)
action.context_click(doubleClick).perform() # it performs right click action
action.double_click(doubleClick).perform()  # this line will double click the element

alert1 = driver.switch_to.alert
print(alert1.text)
assert "You double clicked me!!!, You got to be kidding me" == alert1.text
alert1.accept()