from selenium.webdriver.common.by import By
import time


def test_add_to_basket_button_presented(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button, "'Add to basket' button not presented"
    print(f"Button text is '{button.text}'")
