# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.test import TestCase
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
#
# # Create your tests here.
#
#
# class SanityTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#         super(SanityTestCase, self).setUp()
#
#     def tearDown(self):
#         self.browser.quit()
#         super(SanityTestCase, self).tearDown()
#
#     def test_register(self):
#         browser = self.browser
#         browser.get('http://127.0.0.1:8000/mgmt/')
#         self.assertTrue('Tutorial' in browser.title)
#
#
# class UntitledTestCase(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.katalon.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_register(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:8000/mgmt/instructors/add/")
#         driver.find_element_by_id("id_first_name").click()
#         driver.find_element_by_id("id_first_name").clear()
#         driver.find_element_by_id("id_first_name").send_keys("THISGUY")
#         driver.find_element_by_id("id_last_name").click()
#         driver.find_element_by_id("id_last_name").clear()
#         driver.find_element_by_id("id_last_name").send_keys("ISHILARIOUS")
#         # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_course_offered | label=Basics]]
#         driver.find_element_by_xpath("//option[@value='6']").click()
#         # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_course_offered | label=CS Basics]]
#         driver.find_element_by_xpath("//option[@value='30']").click()
#         # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_course_offered | label=CS Advanced]]
#         driver.find_element_by_xpath("//option[@value='31']").click()
#         driver.find_element_by_xpath("//button[@type='submit']").click()
#         self.assertTrue(driver.find_element_by_xpath("//h1"), "HOLY MACARONI THIS WORKED")
#
#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
#     def is_alert_present(self):
#         try:
#             self.driver.switch_to.alert()
#         except NoAlertPresentException:
#             return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to.alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
