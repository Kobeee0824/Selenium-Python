from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()

#1AlertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")

#1AlertButton.click()

# Since di kaya ma inspect yung alert na notification pop-up, ganito gagawin
#1alert = driver.switch_to.alert
#1alert_text = alert.text
#1print(alert_text)
#1time.sleep(3)
#1alert.accept()
#1time.sleep(3)


#sa taas is kapag ok, itong sa baba naman is cancel
#2AlertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")

#2AlertButton.click()

# Since di kaya ma inspect yung alert na notification pop-up, ganito gagawin
#2alert = driver.switch_to.alert
#2alert_text = alert.text
#2print(alert_text)
#2time.sleep(3)
#2alert.dismiss()
#2time.sleep(3)

#sa taas is kapag ok, itong sa baba naman is cancel
AlertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")

AlertButton.click()

# Since di kaya ma inspect yung alert na notification pop-up, ganito gagawin
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(3)
alert.send_keys("This is a Selenium with python tutorial on Handling Alerts")
alert.accept()
time.sleep(3)