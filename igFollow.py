from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# your login username and password
user = InstagramBot('username', 'password')

user.login()
# follow 
user.Follow('sbm_label', 30)

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Opera()

    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(15)
        bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(5)
        
    def Follow(self, name, number):
        bot = self.bot
        bot.get('https://www.instagram.com/'+name)
        time.sleep(10)
        bot.find_element_by_xpath('//a[@href ="/'+ name + '/followers/"]').click()
        time.sleep(10)
        hrefs = bot.find_elements_by_tag_name('a')
        users_hrefs = [elem.get_attribute('href') for elem in hrefs]
        slice_array = users_hrefs[29:]
        for i in range(1, len(slice_array)+1):
            time.sleep(5)
            bot.get(slice_array[i])
            try:
                postsContainer = bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div')
                postHrefs = postsContainer.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in postHrefs]
                for pic_href in pic_hrefs:
                    bot.get(pic_href)
                    time.sleep(5)
                    bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
                    time.sleep(5)
                time.sleep(5)
            except Exception as e:
                print("empty")
                time.sleep(5)
