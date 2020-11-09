from selenium import webdriver


class MessageSender:
    def send_message(self, contact, message):
        driver = webdriver.Chrome()
        driver.get('https://instagram.com')