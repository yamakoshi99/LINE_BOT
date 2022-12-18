from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_username = browser.find_element_by_id('password')
elem_username.send_keys('kohei')
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()
elem = browser.find_element_by_id('name')
name = elem.text
elem = browser.find_element_by_id('company')
company = elem.text
elem = browser.find_element_by_id('birthday')
birthday = elem.text
elem = browser.find_element_by_id('come_from')
come_from = elem.text
elem = browser.find_element_by_id('hobby')
hobby = elem.text
