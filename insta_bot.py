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

class InstaBot:
    def __init__(self):
        # service = Service('./geckodriver')
        # options = Options()
        # # options.set_preference("intl.accept_languages", "pt,pt-BR")
        # # options.set_preference("dom.webnotifications.enabled", False)
        # self.driver = webdriver.Firefox(
        #     options=options, service=service
        # )
        driver = "a"

    @staticmethod
    def digite_que_nem_gente(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 2) /60)

    def giveaway_data(self, id = "all"):
        time.sleep(5)
        #self.rolar_no_explorar(30)
        if(id=="leao"):
            link = "https://www.instagram.com/p/Cp3gMsqLd_3"
            follow_link = "https://instagram.com/premiando.geral"
        return {'link': link, 'follow_link': follow_link}

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
            usuario="rachidgomesm"
            senha=mesma
        elif(perfil==4 or perfil=="marie"):
            usuario="mariemalufdog"
            senha="mariezita"
        elif(perfil==5 or perfil=="sortudo"):
            usuario="rachmaluf"
            senha=mesma
        elif(perfil==6 or perfil=="thimianss"):
            usuario="thimianss"
            senha=mesma
        elif(perfil==7 or perfil=="vempropai"):
            usuario="rachgomesss"
            senha=mesma
        elif(perfil==8 or perfil=="ganhareii"):
            usuario="_rachidm"
            senha=mesma
        elif(perfil==9 or perfil=="vou"):
            usuario="rachidgomess"
            senha="mariza123"
        #elif(perfil==10 or perfil=="queijo"):
        #   usuario="queijodobao"
        #  senha=mesma
        elif(perfil==11 or perfil=="vemmg"):
            usuario="rachgomes"
            senha=mesma
        elif(perfil==12 or perfil=="ganhadore"):
            usuario="rachidmaluuf"
            senha="mariza123"
        elif(perfil==13 or perfil=="ganharei"):
            usuario="rachidgomesss"
            senha=mesma
        elif(perfil==14 or perfil=="sorte"):
            usuario="rachidgmm"
            senha=mesma
        elif(perfil==15 or perfil=="ganhou"):
            usuario="rachgmm"
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
    
a=InstaBot()