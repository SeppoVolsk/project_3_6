import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_is_displayed(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"), \
        "The button was not found!"

