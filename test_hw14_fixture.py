import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://rozetka.com.ua/ua/"
link1 = "https://casenik.com.ua"


class TestSite():

    @classmethod
    def setup_class(self):
        print("\n Start browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\n Quit browser for test suite..")
        self.browser.quit()

    def test_is_button_search(self, test_1):
        self.browser.get(link)
        self.browser.find_element(By.XPATH,
                                  "//button[@class='button button_color_green button_size_medium search-form__submit']")

    def test_is_basket_link_on_the_main_page(self, test_1):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//rz-cart[@class='header-actions__component']")

    def test_select_checkboxes(self, test_1):
        self.browser.get(link1)
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//a[@href='category/Chehly']").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//label[text()='Xiaomi                ']").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//label[text()='10 - 20                ']").click()
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//label[text()='Есть в наличии                ']").click()
        time.sleep(3)


@pytest.fixture(scope="class")
def test_1():
    print("\nWelcome")


@pytest.fixture(autouse=True)
def test_2():
    yield
    print("\nTest done")
