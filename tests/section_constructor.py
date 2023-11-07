from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators


def test_go_to_bread(browser):
    """
    Тест перехода к разделу Булки:
    """
    browser.find_element(*MainPageLocators.constructor_link_sauce).click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located
                                    (MainPageLocators.constructor_text_sauce))
    browser.find_element(*MainPageLocators.constructor_link_bread).click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located
                                    (MainPageLocators.constructor_text_bread))
    bread = browser.find_element(*MainPageLocators.constructor_text_bread).text

    assert "Булки" in bread


def test_go_to_sauce(browser):
    """
       Тест перехода к разделу Соусы:
       """
    browser.find_element(*MainPageLocators.constructor_link_sauce).click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        MainPageLocators.constructor_text_sauce))
    sauce = browser.find_element(*MainPageLocators.constructor_text_sauce).text

    assert "Соусы" in sauce


def test_go_to_fillings(browser):
    """
    Тест перехода к разделу Начинки:
    """
    browser.find_element(*MainPageLocators.constructor_link_fillings).click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        MainPageLocators.constructor_text_fillings))
    fillings = browser.find_element(*MainPageLocators.constructor_text_fillings).text

    assert "Начинки" in fillings
