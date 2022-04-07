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

class InstagramBot:
    def __init__(self):
        service = Service('./chromedriver')
        options=Options()
        # options.set_preference("intl.accept_languages", "pt,pt-BR")
        # options.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Chrome(
            options=options, service=service
        )

    def lista_seguindo(self, id):
        seguindo=[]
        arquivoCerto=id+"_ListaCerta.txt"
        arquivoAux=id+"_seguindo.txt"
        with open(arquivoAux, encoding="utf8") as arq:
            seguindoAux = arq.readlines()
            seguindoAux = [x.strip() for x in seguindoAux]
            contar=-1
            for item in seguindoAux:
                if(contar%3==0):
                    if('Verificado' in item):
                        contar-=1
                    elif any(x.isupper() for x in item):
                        """"Testa se tem maiúsculo na string"""
                        contar+=1
                    else:
                        seguindo.append(item)
                contar+=1
            print(seguindo)
        with open(arquivoCerto, "w", encoding="utf8") as arq1:
            for item in seguindo:
                arq1.write(item+"\n")
            arq1.close()
        with open(id+"_Relatório.txt", "a+") as arquivo:
                arquivo.write("\nLista obtida, "+str(len(seguindo))+" perfis obtidos")
                arquivo.close()
                print("\nLista obtida, "+str(len(seguindo))+" perfis obtidos")
        
    def login(self, perfil):
        driver = self.driver
        time.sleep(5)
        mesma="Mariza123"
        if(perfil==1 or perfil=="tgmm"):
            usuario="tgmmbr"
            senha=mesma
        elif(perfil==2 or perfil=="tim" ):
            usuario="timastecamaia"
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
        elif(perfil==10 or perfil=="queijo"):
            usuario="queijodobao"
            senha=mesma
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
            time.sleep(5)
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
            time.sleep(12)
            print("Login feito, conta: " + usuario+" ( "+str(perfil)+" )")
        except Exception as e:
            pass

    def seguirTodos(self, arquivo):
        driver = self.driver
        contar=0
        true=0
        with open(arquivo, "r") as arq:
            lista=arq.readlines()
            lista = [x.strip() for x in lista]
            print("Leu "+str(len(lista))+" linhas")
            arq.close()
        while contar<len(lista):
            try:
                for i in lista:
                    time.sleep(10)
                    contar+=1
                    if(contar%42==0):
                        self.rolar_no_explorar(90)
                        time.sleep(10)
                    else:
                        time.sleep(20)
                    if(self.seguir(i)):
                        true+=1
                    else:
                        print("Conferir perfil: "+i)
            except Exception as e:
                print(e)
                print("!!!!!  TENTOU SAIR  !!!!!")
                break
                
        
        return contar, true

    def seguir(self, perfil):
        driver = self.driver
        try:
            time.sleep(5)
            driver.get("https://www.instagram.com/"+perfil)
            time.sleep(10)
            seguindo=driver.find_element_by_xpath(
                "//button[contains(text(), 'Seguir')]"
            )
            seguindo.click()
            driver.find_element_by_xpath(
                "//button[contains(text(), 'OK')]"
            )
            time.sleep(5)
            return True
        except Exception as e:
            return False

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

    def trocar_conta(self):
        driver = self.driver
        time.sleep(3)
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        driver.find_element_by_xpath(
            "//div[contains(text(), 'Mudar')]"
        ).click()
        time.sleep(5)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Entrar em uma já conta existente')]"
        ).click()
        time.sleep(5)

    def sair(self):
        driver = self.driver
        driver.quit()

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

    def main(self, perfil, id):
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

        elements = driver.find_elements_by_xpath("//*[text()='Follow']")
        for i in elements:
            i.click()
            time.sleep(30)
        self.rolar_no_explorar(30)
        self.relatorio(len(elements), perfil, id)


RachidBot = InstagramBot()
RachidBot.main(int(sys.argv[1]) ,sys.argv[2])
RachidBot.sair()