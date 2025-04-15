import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element("xpath","//button[@type = 'submit']")
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element("xpath","//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element("xpath", "//input[@id='answer']")
    input1.send_keys(y)
    time.sleep(1)
    btn2 = browser.find_element("xpath", "//button[@type = 'submit']")
    btn2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()