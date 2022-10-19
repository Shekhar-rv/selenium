from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Point to where your browser is installed
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
# options.add_argument("--start-maximized")

# Path to chromedriver driver on your system
chrome_driver_binary = Service("./selenium_driver/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_binary, options=options)
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# Wait for 3 seconds to load the page
driver.implicitly_wait(3)

# Take care of pop-up on the page
try:
    no_button = driver.find_element(By.ID, "at-cm-no-button")
    no_button.click()
except Exception as ex:
    print("No pop-up found", ex)

value_1 = driver.find_element(By.ID, "sum1")
value_2 = driver.find_element(By.ID, "sum2")

value_1.send_keys("5")
value_2.send_keys("10")

# Find the get total button using css selector and click it.
get_total = driver.find_element(
    By.CSS_SELECTOR, 
    "button[onclick='return total()']"
)
get_total.click()