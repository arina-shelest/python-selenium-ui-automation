import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def _fill_registration_form(self, link):
        self.browser.get(link)

        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Jack")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Jonson")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test_mail@gmail.com")
        self.browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first").send_keys("+491111111111")
        self.browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second").send_keys("Address test")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text

    def test_registration_success(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self._fill_registration_form(link)
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_bug_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self._fill_registration_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
