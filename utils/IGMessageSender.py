from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
from time import sleep


class IGMessageSender:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get('https://instagram.com')
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(), "Accept")]').click()
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(os.getenv("USERNAME"))
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(os.getenv("PASSWORD"))
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()

    def send_message(self, contact, message):
        self.driver.get('https://instagram.com/'+contact)
        sleep(3)
        self.driver.find_element_by_xpath('//button[contains(text(), "Message")]').click()
        sleep(3)
        elem = self.driver.switch_to.active_element
        elem.send_keys(message)
        elem.send_keys(Keys.RETURN)
        sleep(3)

    def close_driver(self):
        self.driver.quit()
