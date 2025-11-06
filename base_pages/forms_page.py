import time

from selenium.webdriver.common.by import By


class FormsPage:
    def __init__(self,driver):
        self.driver =driver
        self.FIRST_NAME =(By.ID,"firstName")
        self.LAST_NAME=(By.ID,"lastName")
        self.EMAIL =(By.ID,"userEmail")
        self.GENDER=(By.CSS_SELECTOR, "label[for='gender-radio-1']")
        self.MOBILE=(By.ID,"userNumber")
        self.SUBMIT=(By.ID,"submit")

    def open_form(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def fill_form(self,first,last,email,mobile):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.GENDER).click()
        self.driver.find_element(*self.MOBILE).send_keys(mobile)
        # ✅ Scroll into view to avoid click interception
        submit_btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)

        # ✅ Optional: small pause helps in slow environments
        self.driver.execute_script("window.scrollBy(0, -100)")  # adjust position slightly up
        time.sleep(5)
        submit_btn.click()
