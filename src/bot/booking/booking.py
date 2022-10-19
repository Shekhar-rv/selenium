from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from booking import constants as const

# Here the code will house a class with instances of the booking

BROWSER_PATH = config("BROWSER_PATH")
DRIVER_PATH = config("DRIVER_PATH")

class Booking():
    def __init__(self, browser_path=BROWSER_PATH, driver_path=DRIVER_PATH, teardown=False):
        """ This class takes in the path to the browser and the driver and initializes the driver """
        self.browser_path = browser_path
        self.driver_path = driver_path
        self.teardown = teardown
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.browser_path
        self.chrome_driver_binary = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=self.chrome_driver_binary, options=self.options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def change_currency(self, currency:str=None):
        currency_element = self.driver.find_element(
            By.CSS_SELECTOR, 
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_destination(self, destination:str=None):
        destination_element = self.driver.find_element(By.NAME, "ss")
        destination_element.clear()
        destination_element.send_keys(destination)
        first_suggestion_element = self.driver.find_element(
            By.CSS_SELECTOR,
            'li[data-i="0"]'
        )
        first_suggestion_element.click()

    def select_dates(self, check_in_date:str=None, check_out_date:str=None):
        check_in_element = self.driver.find_element(
            By.CSS_SELECTOR, 
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        
        check_out_element = self.driver.find_element(
            By.CSS_SELECTOR, 
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()