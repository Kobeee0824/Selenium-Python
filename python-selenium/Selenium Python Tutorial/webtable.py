from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()

# para magscroll down at makita yung table
driver.execute_script("window.scrollTo(0, 700)")

table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(row_count)

target_value = "Australia"
found = False

#isa isa table data checheck niya sa row
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found Value {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target value {target_value} not found")