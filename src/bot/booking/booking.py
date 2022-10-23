from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from booking import constants as const
from booking.booking_filteration import BookingFilterations
from selenium.webdriver.common.keys import Keys


# Here the code will house a class with instances of the booking

BROWSER_PATH = config("BROWSER_PATH")
DRIVER_PATH = config("DRIVER_PATH")

class Booking():
    def __init__(self, browser_path=BROWSER_PATH, 
    driver_path=DRIVER_PATH, 
    teardown=False
    ):
        """ 
        This class takes in the path to the browser and the 
        driver and initializes the driver.
        """
        self.browser_path = browser_path
        self.driver_path = driver_path
        self.teardown = teardown
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.browser_path
        self.chrome_driver_binary = Service(self.driver_path)
        self.driver = webdriver.Chrome(
            service=self.chrome_driver_binary, 
            options=self.options
        )
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
        """  
        Enter the currency you want to use.
        """
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
        """
        Enter the destination you want to search for. The function will
        wait 5 seconds before clicking on the selected destination. 
        """
        destination_element = self.driver.find_element(By.NAME, "ss")
        destination_element.clear()
        try:
            destination_element.send_keys(destination)
            first_suggestion_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'li[data-i="0"]')))
            first_suggestion_element.click()
        except Exception as e:
            print(e)

    def select_dates(self, check_in_date:str=None, check_out_date:str=None):
        """ 
        Enter checkin and checkout dates for the selected destination. 
        The dates should be in the format YYYY-MM-DD. The function will 
        wait 5 seconds before clicking on the selected dates.
        """
        try:
            check_in_element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (
                    By.CSS_SELECTOR, 
                    f'td[data-date="{check_in_date}"]'
                    )
                )
            )
        except Exception as e:
            print(e)
        else:
            check_in_element.click()
        try:
            check_out_element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (
                    By.CSS_SELECTOR, 
                    f'td[data-date="{check_out_date}"]'
                    )
                )
            )
        except Exception as e:
            print(e)
        else:
            check_out_element.click()

    def select_adults(self, number_of_adults:int=1):
        """  
        Select the number of adults you want to book for.
        """
        adults_element = self.driver.find_element(By.ID, "xp__guests__toggle")
        adults_element.click()

        # while True:
        #     decrease_adults_element = self.driver.find_element(
        #         By.CSS_SELECTOR,
        #         'button[aria-label="Decrease number of Adults"]'
        #     )
        #     decrease_adults_element.click()
        #     # If the number of adults is 1, break out of the loop
        #     # Get the number of adults
        #     number_of_adults = self.driver.find_element(
        #         By.ID, 
        #         "group_adults"
        #     ).get_attribute("value")

        #     if int(number_of_adults) == 1:
        #         break


        increase_adults_element = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(number_of_adults - 2):
            increase_adults_element.click()

    def click_search(self):
        """  
        Click on the search button.
        """
        search_element = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_element.click()

    def filter_search_results(self):
        """  
        Filter the search results. 
        """
        filteration = BookingFilterations(driver=self.driver)
        filteration.apply_star_rating_filter()
