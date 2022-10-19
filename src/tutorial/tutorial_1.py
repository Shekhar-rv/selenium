from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Point to where your browser is installed
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
# options.add_argument("--start-maximized")

# Path to chromedriver driver on your system
chrome_driver_binary = Service("./selenium_driver/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_binary, options=options)
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

# Wait for 3 seconds to load the page
driver.implicitly_wait(3)

# Find the id of the accept cookie button and click accept
download_button = driver.find_element(By.ID, "downloadButton")
download_button.click()

# Find the progress bar and wait for it to be 100%
WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),  # Element to check
        "Complete!",  # Text to check for
    )
)

driver.close()
