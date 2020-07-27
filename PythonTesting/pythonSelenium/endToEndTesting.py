#section 70, 71, 72, 73
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
#//div[@class='card h-100']/div/h4/a - it will have the product name
#product = //div[@class='card h-100']

for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)  # product alreay have the products full locators now we are passing the child one
    #div/h4/a = //div[@class='card h-100']/div/h4/a
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        #Add item to cart
        product.find_element_by_xpath("div[2]/button").click()  # this line will click the add to cart
        driver.find_element_by_css_selector("a[class*='primary']").click()
        #wait = WebDriverWait(product, 5)
        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, "div[class='media-body'] h4")))
        cartProductName = driver.find_element_by_xpath("//div[@class='media-body']/h4").text  # product name after adding into the cart
        print(cartProductName)
        assert productName == cartProductName
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_xpath("//input[@id='country']").send_keys("Ind")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()
confirmationMessage = driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
print(driver.find_element_by_css_selector("div[class*='alert-dismissible']").text)

assert "Success!" and "next few weeks" in confirmationMessage

driver.get_screenshot_as_file("screenshot.png")


# line 23 & 24 giving StaleElementReferenceException



#driver.close()