import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items_body(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(5)
    browser.quit()