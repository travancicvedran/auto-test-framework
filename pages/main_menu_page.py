from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainMenuPage:

    URL = "https://travancicvedran.github.io/ExplosiveGrammar/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def select_category(self, category_name):
        self.wait.until(EC.element_to_be_clickable((By.ID, "dropdownBtn"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@onclick=\"setCategory('{category_name}')\"]"))).click()

    def go_to_level_selection(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='goToLevelSelection()']"))).click()

    def buy_item_from_shop(self, item_id):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='showShopOverlay()']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@data-id='{item_id}']"))).click()

    def is_item_bought(self, item_id):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//button[@data-id='{item_id}']")))
        state = button.get_attribute("data-state")
        return state != "buy"

    def get_secret_credits(self):
        for _ in range(5):
            self.wait.until(EC.element_to_be_clickable((By.ID, "logoImg"))).click()

    def reset_progress(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='showResetOverlay()']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='resetOverlay']/div/div[2]/button/p"))).click()

    def get_credits(self):
        credits_text = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "credits"))).text
        return int(credits_text.split(":")[1].strip())
