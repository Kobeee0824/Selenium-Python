from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

#iframe is parang div na may html sa loob niya
#so kaya may ganitong code is para i-access muna yung html sa loob ng iframe at di yung pinakamain na HTML
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

Text_Editor = driver.find_element(By.ID, "tinymce")
Text_Editor.clear()
Text_Editor.send_keys("This is Selenium with Python Iframe Tutorial")

#remember, since nasa loob ka ng iframe, need mo lumabas para maaccess other HTML elements na nasa labas ng iframe
driver.switch_to.default_content()

Selenium_link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
Selenium_link.click()
time.sleep(3)

