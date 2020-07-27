import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\brkre\\Ram\\Selenium\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries)) # len() used to know the list of option which is related to the passing work ex:ind

for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text) # it print empty because Selenium loads the Dom when it opens the page after wards system updates the value in the dynamic dropdown and the entered element is present in the dropdown, but selenium do not have the knowledge of this update because it will read the Dom again once you refresh or page loads.

#get.attribute() - this method actually fire the event in the Dom and attribute will store whatever value is entered in the dropdown
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

