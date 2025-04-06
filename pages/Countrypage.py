from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Countrypage:
    def __init__(self,driver):
        self.driver = driver

    country_dropdown_xpath = "//*[@id='root']/div/div/div/div/div/select"
    agree_checkbox_xpath = "//*[@id='root']/div/div/div/div/input"
    proceed_button_xpath = "//*[@id='root']/div/div/div/div/button"


    def select_country_dropdown(self):
        country_dropdown = self.driver.find_element(By.XPATH,self.country_dropdown_xpath)
        opt = Select(country_dropdown)
        opt.select_by_visible_text("India")

    def click_agree_checkbox(self):
        self.driver.find_element(By.XPATH,self.agree_checkbox_xpath).click()
    def click_proceed_button(self):
        self.driver.find_element(By.XPATH,self.proceed_button_xpath).click()

