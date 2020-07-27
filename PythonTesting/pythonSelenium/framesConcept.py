# developer uses either iframe or frameset or frame. They mostly uses attributes like frame id or frame name or frame value
# switch_to.frame() method will use to switch to the frame, and it accepts only frame id or frame name or frame value
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Welcome to frames")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
