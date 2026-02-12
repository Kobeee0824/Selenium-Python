from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()


# Switching to TOP Frame

driver.switch_to.frame("frame-top")

# Switching to MIDDLE Frame

driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, "content").text
print("Content in middle frame", content)

# Switch to Default content

driver.switch_to.default_content()

# Switch to Bottom Frame

driver.switch_to.frame("frame-bottom")
content_Bottom = driver.find_element(By.TAG_NAME, "body").text
print("Content in Bottom frame", content_Bottom)



time.sleep(3)

