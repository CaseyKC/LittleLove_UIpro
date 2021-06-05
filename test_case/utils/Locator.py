from selenium.webdriver.common.by import By


class Locator():

    def __init__(self, name, by_type=By.ID, wait_sec=3, value=''):
        self.name = name
        self.by_type = by_type
        self.wait_sec = wait_sec
        self.value = value

    def sett_value(self, value):
        return Locator(self.name, self.by_type, self.wait_sec, value)

