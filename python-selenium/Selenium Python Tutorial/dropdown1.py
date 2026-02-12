from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_element = driver.find_element(By. ID, "dropdown")
target_value = "Option 3"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option is {option.text}")
        break
    else:
        print(f"Option '{option.text}' not found")




#2select = Select(dropdown_element)
#2option_count = len(select.options)

#2expected_count = 3

#2if option_count == expected_count:
    #2print("Test case passed. Count is correct")
#2else:
    #2print("Test case failed. Count is incorrect")

# Select the value by visible text
# Select the value by Index
# Select the option by using a value

#1select.select_by_visible_text("Option 2")
#1select.select_by_index(2)
#1select.select_by_value("2")

time.sleep(5)

# WHAT WE LEARNED?
# 1. How to Interact with Dropdown
# 2. How to use Select Class
# 3. How to use 3 Different methods
# 4. Select by Visible text
# 5. Select by Value
# 6. Select by Index
# 7. How to count the dropdown values
# 8. Loop the dropdown values and if the desired value found, select that value