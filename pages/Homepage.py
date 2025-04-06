from selenium.webdriver.common.by import By
import pytest
import time


class Homepage:
    def __init__(self,driver):
        self.driver = driver

    products_xpath = "//*[@id='root']/div/div[1]/div[1]/div"
    product_name_xpath = "//*[@id='root']/div/div[1]/div/div[i]/h4"
    add_to_cart_xpath = "//*[@id='root']/div/div[1]/div/div[i]/div[3]/button"
    plus_xpath = "//*[@id='root']/div/div[1]/div/div[i]/div[2]/a[2]"
    minus_xpath = "//*[@id='root']/div/div[1]/div/div[i]/div[2]/a[1]"
    quantity_xpath = "//*[@id='root']/div/div[1]/div/div[i]/div[2]/input"

    homepage_url = "https://rahulshettyacademy.com/seleniumPractise/#/"
    brocoli_1kg_xpath = "//*[@id='root']/div/div[1]/div/div[1]/h4"
    brocoli_plus_xpath = "//*[@id='root']/div/div[1]/div/div[1]/div[2]/a[2]"
    brocoli_amount_xpath = "//*[@id='root']/div/div[1]/div/div[1]/div[2]/input"
    brocoli__add_to_cart_xpath = "//*[@id='root']/div/div[1]/div/div[1]/div[3]/button"
    brocoli_add_to_cart_xpath = "//*[@id='root']/div/div[1]/div/div[1]/div[3]/button"
    cart_icon_xpath = "//*[@id='root']/div/header/div/div[3]/a[4]/img"
    proceed_to_checkout_xpath = "//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button"
    place_order_xpath = "//*[@id='root']/div/div/div/div/button"
    "+str(r)+"
    quant_value = ""


    def launch_homapage_url(self):
        self.driver.get(self.homepage_url)
    def select_products(self):
        global quant_value
        no_of_products = self.driver.find_elements(By.XPATH,self.products_xpath)
        for i in range(1,len(no_of_products)):
            product_name = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div["+str(i)+"]/h4")
            # vegetables.append(product_name.text)
            # if fruit_name in vegetables:
            if product_name.text == "Brocolli - 1 Kg" or product_name.text == "Cucumber - 1 Kg" or product_name.text == "Tomato - 1 Kg":
                while True:
                    plusss = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div[" + str(i) + "]/div[2]/a[2]")
                    plusss.click()
                    quantity = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div["+str(i)+"]/div[2]/input")
                    value = quantity.get_attribute("value")
                    quant_value = quant_value
                    if value == "5":
                        break
                    add_to_cart = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div["+str(i)+"]/div[3]/button")
                    add_to_cart.click()

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH,self.cart_icon_xpath).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH,self.proceed_to_checkout_xpath).click()

