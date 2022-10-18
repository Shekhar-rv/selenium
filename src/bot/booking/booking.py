from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from decouple import config
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)