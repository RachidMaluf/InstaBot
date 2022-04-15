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

class InstaBot:
    def __init__(self):
        service = Service('./chromedriver')
        options = Options()
        # options.set_preference("intl.accept_languages", "pt,pt-BR")
        # options.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Chrome(
            options=options, service=service
        )

    @staticmethod
    def digite_que_nem_gente(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 2) /60)

    def driblar(self, link, tempo):
        driver = self.driver
        time.sleep(5)
        driver.get("https://www.instagram.com/explore/")
        for i in range(4,6):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(tempo)
        driver.get(link)
        time.sleep(5)

    def trocar_conta(self):
        driver = self.driver
        time.sleep(3)
        driver.get("https://www.google.com/")
        time.sleep(360)
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        driver.find_element_by_xpath(
            "//div[contains(text(), 'Mudar')]"
        ).click()
        time.sleep(5)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Entrar em uma já conta existente')]"
        ).click()
        print("\nFez logoff")

    def login(self, perfil):
        driver = self.driver
        time.sleep(5)
        mesma="Mariza123"
        if(perfil==1 or perfil=="tgmm"):
            usuario="tgmmbr"
            senha=mesma
        elif(perfil==2 or perfil=="tim" ):
            usuario="malufrachiid"
            senha="mariezita"
        elif(perfil==3 or perfil=="ganhei"):
            usuario="ganheirachid"
            senha=mesma
        elif(perfil==4 or perfil=="marie"):
            usuario="mariemalufdog"
            senha="mariezita"
        elif(perfil==5 or perfil=="sortudo"):
            usuario="rachidsortudo"
            senha=mesma
        elif(perfil==6 or perfil=="thimianss"):
            usuario="thimianss"
            senha=mesma
        elif(perfil==7 or perfil=="vempropai"):
            usuario="vempro.pai"
            senha=mesma
        elif(perfil==8 or perfil=="ganhareii"):
            usuario="rachidganhareii"
            senha=mesma
        elif(perfil==9 or perfil=="vou"):
            usuario="vou.ganhaaar"
            senha="mariza123"
        #elif(perfil==10 or perfil=="queijo"):
        #   usuario="queijodobao"
        #  senha=mesma
        elif(perfil==11 or perfil=="vemmg"):
            usuario="vempramg"
            senha=mesma
        elif(perfil==12 or perfil=="ganhadore"):
            usuario="rachidganhadore"
            senha="mariza123"
        elif(perfil==13 or perfil=="ganharei"):
            usuario="ganhareitenhofe"
            senha=mesma
        elif(perfil==14 or perfil=="sorte"):
            usuario="rachidsorte"
            senha=mesma
        elif(perfil==15 or perfil=="ganhou"):
            usuario="rachidganhou"
            senha="mariza123"
        try:
            time.sleep(0.1)
            driver.get("https://www.instagram.com")
            time.sleep(5)
            user_element = driver.find_element_by_xpath(
                "//input[@name='username']")
            user_element.clear()
            user_element.send_keys(usuario)
            time.sleep(3)
            password_element = driver.find_element_by_xpath(
                "//input[@name='password']")
            password_element.clear()
            password_element.send_keys(senha)
            time.sleep(3)
            password_element.send_keys(Keys.RETURN)
            time.sleep(10)
            # driver.find_element_by_xpath(
            #     "//button[contains(text(), 'Salvar informações')]"
            # ).click()
            # time.sleep(5)
            print("Login feito, conta: " + usuario+" ("+str(perfil)+")")
        except Exception as e:
            pass

    def rolar_no_explorar(self, tempo):
        driver = self.driver
        links_de_posts = []
        time.sleep(5)
        driver.get("https://www.instagram.com/explore/")
        for i in range(random.randint(8, 10)): 
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(tempo)

    def sair(self):
        driver = self.driver
        driver.quit()

    def relatorio(self, true, perfil, id):
        n=0
        """LOOP WHILE SOMENTE PARA DAR NOME AO PERFIL"""
        while n==0:
            if(perfil==1):
                usuario="tgmmbr"
            elif(perfil==2):
                usuario="timastecamaia"
            elif(perfil==3):
                usuario="ganheirachid"
            elif(perfil==4):
                usuario="marie"
            elif(perfil==5):
                usuario="sortudo"
            elif(perfil==6):
                usuario="thimianss"
            elif(perfil==7):
                usuario="vem pro pai"
            elif(perfil==8):
                usuario="ganhareii"
            elif(perfil==9):
                usuario="vou.ganhaaar"
            elif(perfil==10):
                usuario="queijoo"
            elif(perfil==11):
                usuario="vem pra mg"
            elif(perfil==12):
                usuario="rachidganhadore"
            elif(perfil==13):
                usuario="ganharei"
            elif(perfil==14):
                usuario="rachidganheii"
            elif(perfil==15):
                usuario="ganhou"
            elif(perfil==16):
                usuario="sorte"
            n+=1
        with open(id+"_Relatório.txt", "a+") as arquivo:
            arquivo.write("\nBem sucedido!!  --> "+usuario+" ("+str(perfil)+")"+" seguiu "+str(true)+" perfis.\n")
            arquivo.close()
            print("Relatório registrado, perfil:",perfil)
    