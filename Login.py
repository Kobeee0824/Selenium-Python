# Open and control a Chrome browser
from selenium import webdriver

# Used to find elements on the web page
from selenium.webdriver.common.by import By

# Used to pause the program
import time

# Start a new Chrome browser
driver = webdriver.Chrome()

# Make the browser window full screen
driver.maximize_window()

# Username for login
username = "standard_user"

# Password for login
password = "secret_sauce"

# Website login page
login_url = "https://www.saucedemo.com/"

# Open the website
driver.get(login_url)

# Find the username input box
username_field = driver.find_element(By.ID, "user-name")

# Find the password input box
password_field = driver.find_element(By.ID, "password")

# Type username into the box
username_field.send_keys(username)

# Type password into the box
password_field.send_keys(password)

# Find the login button
login_button = driver.find_element(By.ID, "login-button")

# Check that the login button is enabled
assert not login_button.get_attribute("disabled")

# Click the login button
login_button.click()

# Find the title text after login
success_element = driver.find_element(By.CSS_SELECTOR, ".title")

# Check that login was successful
assert success_element.text == "Products"

# Keep the browser open for 60 seconds
time.sleep(60)
