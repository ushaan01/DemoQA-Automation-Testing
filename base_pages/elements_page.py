from selenium.webdriver.common.by import By


class ElementsPage:
    def __init__(self,driver):
        self.driver= driver
        self.FULL_NAME = (By.ID,"userName")
        self.EMAIL =(By.ID,"userEmail")
        self.CURRENT_ADD =(By.ID,"currentAddress")
        self.PERMANENT_ADD =(By.ID,"permanentAddress")
        self.SUBMIT=(By.ID,"submit")
        self.OUTPUT =(By.ID,"output")

    def open_text_box(self):
        self.driver.get("https://demoqa.com/text-box")

    def fill_text_box(self,name,email,current,permanent):
        self.driver.find_element(*self.FULL_NAME).send_keys(name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.CURRENT_ADD).send_keys(current)
        self.driver.find_element(*self.PERMANENT_ADD).send_keys(permanent)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.SUBMIT))

    def get_output(self):
        return self.driver.find_element(*self.OUTPUT).text

