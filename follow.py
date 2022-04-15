from ast import In
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import timeit
from webbrowser import get
import pdb
import sys
from insta_bot import InstaBot

class Follow(InstaBot):
    def __init__(self):
        super().__init__()


    def rolar_no_explorar(self, tempo):
        driver = self.driver
        links_de_posts = []
        time.sleep(5)
        driver.get("https://www.instagram.com/explore/")
        for i in range(random.randint(8, 10)): 
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(tempo)

    def scroll_down(self, scroll):
        driver = self.driver
        div = driver.find_element_by_css_selector(".isgrP")
        for i in range(0,scroll):
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div)
            time.sleep(2)


    def mainnn(self, perfil, id):
        driver = self.driver
        self.login(perfil)        
        if(id=="iphone"):
            link="https://www.instagram.com/sorteiosjohn/"
            scroll = 7
        elif(id=="big"):
            link="https://www.instagram.com/projeto_onix_"
            scroll = 14
        driver.get(link)
        time.sleep(5)
        driver.find_element_by_xpath("//*[text()=' following']").click()
        time.sleep(2)
        self.scroll_down(scroll)

        user_list = driver.find_elements_by_xpath("//*[text()='Follow']")
        user_list.reverse()
        for user in user_list:
            try:
                #pdb.set_trace()
                user.click()
                time.sleep(30)
            except Exception as e:
                print(e)
                pass
        self.rolar_no_explorar(30)
        self.relatorio(len(user_list), perfil, id)


follow = Follow()
follow.mainnn(int(sys.argv[1]) ,sys.argv[2])
follow.sair()