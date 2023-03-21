from ast import In
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import timeit
from webbrowser import get
import pdb
import sys
from insta_bot import InstaBot
import re

class Follow(InstaBot):
    def __init__(self):
        service = Service('./geckodriver')
        options = Options()
        # options.set_preference("intl.accept_languages", "pt,pt-BR")
        # options.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            options=options, service=service
        )

    # def rolar_no_explorar(self, tempo):
    #     driver = self.driver
    #     links_de_posts = []
    #     time.sleep(5)
    #     driver.get("https://www.instagram.com/explore/")
    #     for i in range(random.randint(8, 10)): 
    #         driver.execute_script(
    #             "window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(tempo)

    def get_link(self, id):
        driver = self.driver
        time.sleep(5)
        dict = self.giveaway_data(id)
        return dict["follow_link"]

    def scroll_down(self, scroll):
        driver = self.driver
        time.sleep(2)
        div = driver.find_element_by_css_selector("._aano")
        for i in range(0,scroll):
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div)
            time.sleep(2)

    def open_box(self, scroll):
        driver = self.driver
        
        time.sleep(5)
        driver.find_element_by_xpath("//*[text()=' following']").click()
        time.sleep(2)
        self.scroll_down(scroll)
        time.sleep(2)

    def follow_user(self):
        driver = self.driver
        time.sleep(2)
        main_user = driver.find_elements_by_xpath("//*[text()='Follow']")
        if len(main_user )!= 0:
            main_user[0].click()
        time.sleep(2)

    def following_number(self):
        driver = self.driver
        content = driver.find_element_by_xpath("//meta[@property='og:description']").get_attribute("content")
        regexp = re.compile(', (\d+) Following')

        return int( regexp.search(content)[1] )


    def get_list(self):
        driver = self.driver
        user_list = driver.find_elements_by_xpath("//*[text()='Follow']")

        if self.sanitize_list():
            del user_list[0:10]
        return user_list

    def sanitize_list(self):
        driver = self.driver
        suggestion = driver.find_elements_by_xpath("//*[text()='Suggested']")
        if len(suggestion)!= 0:
            return True
        else:
            return False

    def prepare_to_follow(self, link):
        driver = self.driver
        time.sleep(5)
        driver.get(link)
        time.sleep(5)
        number = self.following_number()
        self.follow_user()

        scroll_factor = int (number / 9) + 1
        self.open_box(scroll_factor)
        user_list = self.get_list()

        if len(user_list) == 0:
            print("ALREADY FOLLOWING THEM ALL  =D")
            return True

        return user_list


    def main(self, perfil, id):
        driver = self.driver
        self.login(perfil)
        link = self.get_link(id)

        #pdb.set_trace()
        count = 0
        while True:
            user_list = self.prepare_to_follow(link)
            if user_list == True:
                break 

            #pdb.set_trace()
            for user in user_list:
                try:
                    user.click()
                    count += 1
                    time.sleep(10)
                except Exception as e:
                    print(e)
                    pass
                if (user_list.index(user) + 1) % 10 == 0:
                    self.rolar_no_explorar(10)
                    driver.get(link)
                    break
                
        self.relatorio(count, perfil, id)


follow = Follow()
follow.main(int(sys.argv[1]) ,sys.argv[2])
follow.sair()