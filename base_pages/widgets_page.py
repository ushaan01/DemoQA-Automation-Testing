from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class WidgetsPage:
    def __init__(self,driver):
        self.driver=driver
        self.SLIDER=(By.XPATH,"//input[@type='range']")
        self.SLIDER_VALUE=(By.ID,"sliderValue")

    def open_slider(self):
        self.driver.get("https://demoqa.com/slider")

    def move_slider(self,value):
        slider=self.driver.find_element(*self.SLIDER)
        actions=ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(value,0).release().perform()

    def get_value(self):
        return self.driver.find_element(*self.SLIDER_VALUE).get_attribute("value")
