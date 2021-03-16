import telebot
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
from comments import commentaries

bot = telebot.TeleBot('1696728315:AAG7PwNqsyj6d2r9yZ59YceuFOzqUUhdavs')


@bot.message_handler(commands=['start'])
def starts(message):
    browser = webdriver.Chrome('chromedriver.exe')

    browser.get('https://instagram.com')
    time.sleep(3.5)

    browser.find_element_by_name('username').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('password').send_keys(Keys.ENTER)
    time.sleep(3)

    one_link = []

    try:
        def sendComment():
            global send_comment
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
                    send_comment = browser.find_element_by_class_name('Ypffh')
                    send_comment.click()

                    send_comment = browser.find_element_by_class_name('Ypffh')
                    send_comment.send_keys(commentaries())
                    time.sleep(2)

                    send_comment.send_keys(Keys.ENTER)
                    time.sleep(5)

    except Exception:
        bot.send_message(message.chat.id, 'Ошибка. Программа приостоновлена')

    while True:
        sendComment()


bot.polling()