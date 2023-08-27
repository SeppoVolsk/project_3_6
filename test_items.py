import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
locator = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"


def test_add_button_is_displayed(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, locator), \
        "The button was not found!"

