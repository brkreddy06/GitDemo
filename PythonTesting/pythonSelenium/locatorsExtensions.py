from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")

driver.maximize_window()

driver.find_element_by_css_selector("#username").send_keys("abcdef")  # CSS
driver.find_element_by_css_selector(".password").send_keys("Welcome")  #CSS
driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()

#//tagname[text()=’xxx’]
driver.find_element_by_xpath("//a[text()='Cancel']").click()

#grand parent travel xpath: //form[@id='login_form']/div[@id='usernamegroup']/label or //form[@id='login_form']/div[1]/label  -> if it has more than 1 div tagName
print(driver.find_element_by_xpath("//form[@id='login_form']/div[1]/label").text)  # print username
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(2)").text) # Remember me
print(driver.find_element_by_xpath("//form[@name='login']/label").text)  # print password





