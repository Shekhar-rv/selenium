from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BookingFilterations():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating_filter(self, star_rating:int=5):
        """
        Apply the star rating filter.
        """
        try:
            star_filtering_box =  WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(
                        (
                        By.ID,
                        "filter_class"
                         )
                    )
            )
            star_child_elements = star_filtering_box.find_elements(
                By.CSS_SELECTOR,
                "*"
            )
            print(len(star_child_elements))
        except Exception as ex:
            print(ex)