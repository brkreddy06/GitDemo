from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
childWindow = driver.window_handles[1]  # it will have the child window
driver.switch_to.window(childWindow)  # this line will switch to child window
print(driver.find_element_by_tag_name("h3").text)  # this print the heading of the child window
driver.close()  # this line will close child window
driver.switch_to.window(driver.window_handles[0])  # it will move back to parent window
print(driver.find_element_by_tag_name('h3').text)  # it will print parent window title

assert "Opening a new window" == driver.find_element_by_tag_name('h3').text

