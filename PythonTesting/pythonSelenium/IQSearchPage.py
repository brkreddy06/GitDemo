#IQ4 - Assignment - Verify is search functionality in home page is working. 3 ber, 3 products = x, y, z

import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
#list = []

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
vegNames = driver.find_elements_by_xpath("//div[@class='products']/div/h4")
sum = 0
for vegName in vegNames:
    print(vegName.text)
    sum = sum + int(vegName.text)
print(sum)

    #list.append(vegName.text)

#print("The displayed products after search : ", " ", list)

# i printed 3 products names but don't know how to use the assert method to compare both searched products = displayed products

