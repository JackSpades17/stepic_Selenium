from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.implicitly_wait(5)
    button = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_xpath('//button[text()="Book"]')
    button.click()

    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    y_element= browser.find_element_by_id("answer")
    y_element.send_keys(y)
    browser.execute_script("window.scrollBy(100, 100);")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    time.sleep(16)
    browser.quit()