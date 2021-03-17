import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from comments import commentaries
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
browser = webdriver.Chrome(executable_path="/home/instabot/chromedriver", options=options)

# browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com')
time.sleep(5)

username = 'gosmanager'
password = '020601Aa'

browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(3)

one_link = []

try:
    def sendComment():
        global one_link
        print('Начало цикла')
        if len(one_link) > 30:
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
                time.sleep(3)
                send_comment = browser.find_element_by_class_name('Ypffh')
                send_comment.click()

                send_comment = browser.find_element_by_class_name('Ypffh')
                send_comment.send_keys(commentaries())
                time.sleep(2)

                send_comment.send_keys(Keys.ENTER)
                time.sleep(5)

except Exception as ex:
    print(ex)

while True: