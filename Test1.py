import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com.ng/")
driver.implicitly_wait(4)

search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.click()
search.send_keys("methodology")
# object of ActionChains
a = ActionChains(driver)
# identify element
m = driver.find_element(By.CLASS_NAME, "wM6W7d")
# hover over element
a.move_to_element(m).click().perform()
time.sleep(10)
