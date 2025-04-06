from selenium.webdriver.common.by import By


class Cartpage:
    def __init__(self,driver):
        self.driver = driver

    place_order_xpath = "//*[@id='root']/div/div/div/div/button"
    cart_quantity_xpath = "//*[@id='productCartTables']/tbody/tr/td[3]/p"

    def click_place_order(self):
        self.driver.find_element(By.XPATH,self.place_order_xpath).click()

    def cart_quantity_text(self):
        return self.driver.find_element(By.XPATH,self.cart_quantity_xpath).text

