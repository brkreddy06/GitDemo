#IQ1 - Validate whether products selected in page 1 are showing in page 2 check page
#IQ2 - Verify if price decreases on discount coupon
#IQ3 - Verify if the sum of products in checkout page matches with Total Amount


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.implicitly_wait(5)

list1 = []
list2 = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button - child locator
#//div[@class='product-action']/button/parent::div/parent::div/h4 - child to parent traversal
for button in buttons:
    #print(button.find_element_by_xpath("parent::div/parent::div/h4").text)  #child locator already stored in buttons variable so no need to provide entire xpath
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1) # line 21 = line 24, just for comparing purpose we are storing in list

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

vegies = driver.find_elements_by_css_selector("p.product-name")  # storing the list of vegitables in the variable

for veg in vegies:
    list2.append(veg.text)
print(list2)
del list2[3:6]  # 3 empty spaces are added in the list2, to com
# pare with list1 then need to delete extra spaces in list2
print(list2)

#IQ1
assert list1 == list2
#IQ2
originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
print(float(discountAmount))
print(int(originalAmount))

assert float(discountAmount) < int(originalAmount)   # converting string into float and int, because originalAmount & discountAmount variable returns string

print(driver.find_element_by_css_selector("span.promoInfo").text)

#IQ3
vegAmount = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in vegAmount:
    sum = sum + int(amount.text)
print(sum)

totalAmount = int(driver.find_element_by_css_selector(".totAmt").text)
print(totalAmount)

assert sum == totalAmount

