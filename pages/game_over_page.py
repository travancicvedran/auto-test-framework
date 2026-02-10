from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GameOverPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 65)

    def is_loaded(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "gameOverText")))
