from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--star-maximized")  # it will maximize the browser at backend
chrome_options.add_argument("headless")  # it will display the browser
chrome_options.add_argument("--ignore-certificate-errors") # it will ignore all the certificate popups

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
