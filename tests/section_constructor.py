from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_bread(browser, enter_on_main):
    browser.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]")))
    browser.find_element(By.XPATH, ".//span[text()='Булки']").click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[1]")))
    bread = browser.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[1]").text

    assert "Булки" in bread


def test_go_to_sauce(browser, enter_on_main):
    browser.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]")))
    sauce = browser.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]").text

    assert "Соусы" in sauce


def test_go_to_fillings(browser, enter_on_main):
    browser.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[3]")))
    fillings = browser.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[3]").text

    assert "Начинки" in fillings
