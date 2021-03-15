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

one_link = [' ']

def sendComment():
    links_posts = browser.find_elements_by_tag_name('a')
    posts_urls = [item.get_attribute('href') for item in links_posts if '/p/' in item.get_attribute('href')]
    time.sleep(2)
    browser.get('https://instagram.com/yasinzingiev')
    time.sleep(3)
    if posts_urls[0] != one_link[-1]:
        one_link.append(posts_urls[0])
        while range(3):
            browser.get(posts_urls[0])
            send_comment = browser.find_element_by_class_name('Ypffh')
            send_comment.click()
            send_comment = browser.find_element_by_class_name('Ypffh')
            send_comment.send_keys('Тестовый комментарии')
            send_comment.send_keys(Keys.ENTER)
    else:
        print('continue')

while True:
    sendComment()