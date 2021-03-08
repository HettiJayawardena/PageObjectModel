# This script automate the sign up process in https://www.jedox.com/de/ for a user in Germany using Google chrome Web Browswer.
# IMPORTANT: 1. user should change the path of the project folder in 'project_folder' variable
#            2. make sure all the imported modules are installed in the project
#After filling the relevant fields and signing up, an HTML report will be generated in project folder/Reports


from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import HtmlTestRunner
import os
import sys

project_folder = "C:/Users/MNM-L/PycharmProjects/Signup_Jedox_SignUp"
sys.path.append(project_folder)
chrome_driver_join = os.path.join(project_folder, "Drivers", "chromedriver")
chrome_driver_path = os.path.join(chrome_driver_join).replace("\\", "/")
print(chrome_driver_path)


class SignUpTest(unittest.TestCase):
    baseURL = "https://www.jedox.com/de/"

    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    user_email = input("Enter your valid email:")
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    phone_number = input("Enter your phone number (only numbers are allowed):")
    company = input("Enter your company name:")
    city = input("Enter your city:")
    zip_code = input("Enter your zip code:")
    country = "Germany"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
       
       #cls.assertEqual("Enterprise Performance Management und BI kombiniert in einer Software", cls.driver.title,
        #                "webpage title is not matching")

    def test_signUp(self):
        self.driver.implicitly_wait(10)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']"))).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "// *[ @ id = 'menu-item-65188'] / a / span"))).click()

        self.driver.find_element(By.XPATH, "//*[@id='email-49415066-0497-4a0e-a7e9-ed4c2bfb24c8']").send_keys(
            self.user_email)

        self.driver.find_element(By.ID, "firstname-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.first_name)

        self.driver.find_element(By.ID, "lastname-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.last_name)

        self.driver.find_element(By.ID, "phone-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.phone_number)

        self.driver.find_element(By.ID, "company-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.company)

        self.driver.find_element(By.ID, "city-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.city)

        self.driver.find_element(By.ID, "zip-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").send_keys(
            self.zip_code)

        select_country = Select(self.driver.find_element_by_id("country-49415066-0497-4a0e-a7e9-ed4c2bfb24c8"))
        select_country.select_by_value(self.country)

        select_department = Select(self.driver.find_element_by_id("department-49415066-0497-4a0e-a7e9-ed4c2bfb24c8"))
        select_department.select_by_value("R & D, Engineering")

        self.driver.find_element(By.ID,
                                 "LEGAL_CONSENT.subscription_type_8585633-49415066-0497-4a0e-a7e9-ed4c2bfb24c8").click()

        self.driver.find_element(By.XPATH,
                                 "//*[@id='hsForm_49415066-0497-4a0e-a7e9-ed4c2bfb24c8']/div/div[2]/input").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Test has been completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))
