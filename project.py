import telebot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random

browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://instagram.com')
time.sleep(3.5)

browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(3)

