from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LevelSelectionPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_level_locked(self):
        button = self.driver.find_element(By.CLASS_NAME, "btn2")
        return button.get_attribute("disabled")

    def select_level(self, level_number):
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@onclick='startQuiz({level_number})']"))).click()