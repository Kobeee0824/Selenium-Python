from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.ironspider.ca/forms/checkradio.htm')
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.find_element(By.XPATH, '//input[@value="red"]').click()
#time.sleep(5)
#driver.find_element(By.XPATH, '//input[@value="red"]').click()
#time.sleep(5)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    time.sleep(1)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checked_count = 6
if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')

time.sleep(5)
driver.close()
