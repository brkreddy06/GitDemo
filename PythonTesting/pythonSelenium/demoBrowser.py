from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke the actual browser
# quit() method - it will close all the browsers both parent and child windows
# close() method - it will close only the current window
# back() method - it will take the screen back to the original page
# refresh() - it will refresh the browser

#driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\geckodriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")  #get method to hit the url on browser

print(driver.title)
print(driver.current_url)  # current_url is used to check the accessing URL is correct or not to avoid the cyber attack

driver.get("https://rahulshettyacademy.com/#/mentorship")
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()
