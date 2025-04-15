import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
wait = WebDriverWait(browser,15,poll_frequency=1)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
# Нажимаем кнопку
btn = browser.find_element(By.ID, "book")
btn.click()

# Решаем задачу
x = browser.find_element(By.ID, "input_value").text
answer = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element(By.ID, "answer").send_keys(answer)

# Отправляем
browser.find_element(By.ID, "solve").click()
time.sleep(10)