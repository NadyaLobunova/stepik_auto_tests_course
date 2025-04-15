import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element("xpath","//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element("xpath", "//input[@id='answer']")
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 120);")
    time.sleep(1)
    check_b = browser.find_element("xpath","//input[@id='robotCheckbox']")
    check_b.click()
    radio_b = browser.find_element("xpath","//input[@id='robotsRule']")
    radio_b.click()
    btn = browser.find_element("xpath", "//button[@type = 'submit']")
    btn.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()