from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")

number_of_tabs = len(driver.window_handles)
print(number_of_tabs)
tabs_value = driver.window_handles
print(tabs_value)
Current_tab = driver.current_window_handle
print(Current_tab)
driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
FirstTab = driver.window_handles[0]
if Current_tab != FirstTab: #kaya may ganito kasi need niya mapunta sa second tab na may downloads (yung code sa baba). Or else, mag-error
    driver.switch_to.window(FirstTab)
driver.find_element(By. XPATH, "//span[normalize-space()='Downloads']").click()