from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()

