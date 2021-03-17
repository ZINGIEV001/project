import telebot
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
from comments import commentaries
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


ua = dict(DesiredCapabilities.CHROME)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://instagram.com')

time.sleep(3.5)

browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(3)

one_link = []

try:
    def sendComment():
        if len(one_link) == 33:
            one_link = []
        browser.get('https://instagram.com/app.python')
        time.sleep(3)

        links_posts = browser.find_elements_by_tag_name('a')
        posts_urls = [item.get_attribute(
            'href') for item in links_posts if '/p/' in item.get_attribute('href')]
        time.sleep(2)

        if posts_urls[0] not in one_link:
            one_link.append(posts_urls[0])

            browser.get(posts_urls[0])
            time.sleep(2)

            btn_like = browser.find_element_by_class_name('fr66n')
            btn_like.click()
            time.sleep(0.5)

            for i in range(3):
                global commentaries
                browser.get(posts_urls[0])
                time.sleep(2)
                send_comment = browser.find_element_by_class_name('Ypffh')
                send_comment.click()

                send_comment = browser.find_element_by_class_name('Ypffh')
                send_comment.send_keys(commentaries())
                time.sleep(2)

                send_comment.send_keys(Keys.ENTER)
                time.sleep(2)

except Exception as ex:
    print(ex)

while True:
    sendComment()