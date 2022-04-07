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

    @staticmethod
    def digite_que_nem_gente(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 2) /60)

    def comente(self, id):
        driver = self.driver
        comments = [
                        "O meu bem eu vou fazer um role hj qdo quiser", 
                        "o dia todo e o meu bem", 
                        "graças e vc tem que eu vou te",
                        "a gente não pô mas a gnt fina", 
                        "o que o meu bem não ter", 
                        "de manhã eu não ter um ", 
                        "o que a gente se fala isso", 
                        "o que a gente não vai ser o", 
                        "o dia todo mundo tem uma coisa que ", 
                        "a gente se ver hoje a gente vai ter q comprar um", 
                        "o meu bem eu vou ein man eu não", 
                        "a gente se fala mais tarde eu nãoo sair da pô", 
                        "a minha mãe é um  de boa tarde", 
                        "de um e vc ta joiaa e vc tem q", 
                        "o que o que eu não pô mas a gente não pô mano",
                        "o que eu não ter que é o que "
                        "O pior eh q o jogo do meu lado aq e o pior eh q o jogo",
                        "Eu acho melhor você ir p eu fazer um dia de aula e a gente se encontra",
                        "O que eu vou te avisando pra não ter um dia q eu n tivesse um pouco",
                        "E a gnt ve direitin de uma semana de trabalho e vc tem que ser",
                        "O que eu vou te mandar umas coisas que eu não pô mano e a",
                        "O meu bem você é que eu não pô mano colorado de um dia q eh",
                        "O pior é que é uma coisa q eh o que eu vou te mandar o que eu",
                        "Eu n tivesse um pouco atrasado mas já sei que eu vou te mandar umas",
                        "E a gente se fala mais tarde eu vou ein a gente não vai dar cert",
                        "O pior é que é uma coisa q eh o que eu vou te mandar umas",
                        "Eu vou fazer um teste aí ela me disse o ministro da saúde",
                        "Eu acho que é uma coisa que você é uma coisa que não pô",
                        "Eu n tivesse um pouco de medo da sua roupa de cama de um carro",
                        "O que é que eu vou te mandar umas coisas pra fazer a gente vai",
                        "Eu vou fazer um teste aí você vai ser a gnt ve direitin de umas duas vezes",
                        "E vc não consegue ver a minha vida de uma semana que",
                        "Eu acho q vou estudar a gente vai se ver hoje naoo e a",
                        "O meu bem não pô mas a gnt vai ser a gnt ve se eu",
                        # "😀😃😄😁😆😅😂🤣🥲☺️😊😊🙂🙃😉",
                        # "😌😌🥰🥰😗😙😚😋😛😝😎🥳😏",
                        # "😒😞😔😟😕🙁🙁☹️😖😫😩🥺😢😭😤😠",
                        # "😡🤬🤯😳😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯",
                        # "😦😧😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹",
                        # "👺🤡💩💀☠️👽👾🤖🎃😺😸😹😻😼👏🏽🤝👍🏾",
                        # "👊🏾🤞🏿✌🏾🦿💄💋👄🦷👅👂🏾🦻🏾👃🏿👣👁👀🫀🫁",
                        # "🧠🗣👤👥👶🏿👧🏿🪡🧥🦺👚👕👖🩲🩳👔👗👙🩱👘🥻🩴",
                        # "🥿👠👡👢👞👟🥾🧦🧤🧣🎩🧢👒🎓⛑🪖",
                        # "👑💍👝👜💼🧳👛🕶🥽👓🐱🐭🐶🐹🐹🐰",
                        # "🦊🐻🐼🐨🐨🐯🦁🐮🐷🐸🐸🙈🙉🙊",
                        # "🐒🐔🐧🐦🐤🐣🐥🦆🦅🦇🐺🐗🐴🦄🐝🪱🐛🐌",
                        # "🐌🐞🐜🪰🪲🪳🦟🦗🕷🕸🐙🐍🦎🦖🐙🦑🦐🦀🐡",
                        # "🐠🐟🐬🐳🐋🦈🦭🐊🦛🦏🐪🦒🦘🦬🐃🐂🐄🐎",
                        # "🐖🐏🦙🐐🦌🐕🦙🦌🐩🦙🐐🐕🦃🦚🐓🦩🐇🦝",
                        # "🦨🦡🦦🦥🍃🍂🍄🍄🪨🌾💐🌹🥀🌺🌼🌻🌞🌝🌛🌚"
                    ]
        pessoas = [
            "@marcelohsouzaa",
            "@jp_paschoal_",
            "@vanessa.coost",
            "@luizabuffon",
            "@erick.b_07",
            "@lau",
            "@ana_ifreitas",
            "@pfmmariana",
            "@cibele_alvessr",
            "@rebonatolilian",
            "@suamygoulart",
            "@jessicargmjc",
            "@aniamoutinho_24",
            "@victorialcorrea",
            "@todokaioecesar",
            "@abraao_portes",
            "@carlucioveloso",
            "@kayque_a",
            "@http.flavio_",
            "@nayanafreire14",
            "@j_christian7",
            "@jorge.marcosdocarmo",
            "@keithescariao",
            "@gois.thayna",
            "@wendy_oliveira_",
            "@a.lxce_",
            "@valeriavdt",
            "@leovilain",
            "@_thaismaia_",
            "@camilaselima",
            "@carolrichtic",
            "@maitekretzer",
            "@gabriel_fraga17",
            "@hellen_cr1s",
            "@matheusgomeslopes309",
            "@vallethai",
            "@jordanycirqueira",
            "@maryuchaalmeida",
            "@abreu_m",
            "@felipeeeeramos",
            "@felipe_alves_soares_",
            "@rodrigo.dagama",
            "@rodrigoeduardofpn",
            "@dudu_rbn_",
            "@eoqtorresmo",
            "@pauloh68748",
            "@ingrid.barros.9210",
            "@pedroox_henrique",
            "@c_aio244",
            "@gustavo_canabrava",
            "@arthualvesmartins",
            "@vickofcc",
            "@rnveloso",
            "@byrick.art",
            "@matunaga003",
            "@milanez16",
            "@ovictor1_",
            "@igorgabriel14",
            "@johnatan_80",
            "@papaleguasofc",
            "@guussagazz",
            "@pedroo_xl",
            "@feitosaleo86",
            "@leof_58",
            "@sjulimart",
            "@patrick.pretoo_244",
            "@ic_nuness",
            "@nathanvieirapersonal",
            "@_lucasmoont",
            "@doguinhayt",
            "@jonas_olliver",
            "@thallys_henry",
            "@vulgo_vt_de_bh",
            "@luis_6672",
            "@douglasfernandes.sx",
            "@jarthur_braga",
            "@tacio_170",
            "@kenedyfelip322",
            "@davi_joze_0956",
            "@brennohenriquey",
            "@daviamvm",
            "@geronimo_braz",
            "@arthur_damasceno_04",
            "@viniciosff1",
            "@henriquepmeh",
            "@adailson_77",
            "@lucasgcoficial",
            "@douglas_gomes_028",
            "@charles_gbrl",
            "@paulocesarjb",
            "@alyson__matheus",
            "@_emanuel.caetano",
            "@_paulo_sant0s_",
            "@vinicio_sr.k__",
            "@jarlos.roots",
            "@gedson_tavares",
            "@ismael_erick90",
            "@t.a.y.l.l.o",
            "@luis_cunha88",
            "@lucas.milleno.14",
            "@jp__.06",
            "@_lluis_felipe",
            "@everton_diniz_vlz",
            "@paulo_cesar_021",
            "@ronaldsillva",
            "@ianhudysonleite",
            "@gustaviinho_04",
            "@g.chioda_",
            "@fckonstantin",
            "@luiz_jefferso",
            "@kaynan_kl",
            "@gabrielgomespessoa12",
            "@vitinhoyt122",
            "@luccas_santos__",
            "@caio_montero",
            "@charlesfsjr",
            "@dvd.avila",
            "@evandromarceloo",
            "@mczayra"
            ]
        emojis = [
                        "😀😃😄😁😆😅😂🤣🥲☺️😊😊🙂🙃😉",
                        "😌😌🥰🥰😗😙😚😋😛😝😎🥳😏",
                        "😒😞😔😟😕🙁🙁☹️😖😫😩🥺😢😭😤😠",
                        "😡🤬🤯😳😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯",
                        "😦😧😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹",
                        "👺🤡💩💀☠️👽👾🤖🎃😺😸😹😻😼👏🏽🤝👍🏾",
                        "👊🏾🤞🏿✌🏾🦿💄💋👄🦷👅👂🏾🦻🏾👃🏿👣👁👀🫀🫁",
                        "🧠🗣👤👥👶🏿👧🏿🪡🧥🦺👚👕👖🩲🩳👔👗👙🩱👘🥻🩴",
                        "🥿👠👡👢👞👟🥾🧦🧤🧣🎩🧢👒🎓⛑🪖",
                        "👑💍👝👜💼🧳👛🕶🥽👓🐱🐭🐶🐹🐹🐰",
                        "🦊🐻🐼🐨🐨🐯🦁🐮🐷🐸🐸🙈🙉🙊",
                        "🐒🐔🐧🐦🐤🐣🐥🦆🦅🦇🐺🐗🐴🦄🐝🪱🐛🐌",
                        "🐌🐞🐜🪰🪲🪳🦟🦗🕷🕸🐙🐍🦎🦖🐙🦑🦐🦀🐡",
                        "🐠🐟🐬🐳🐋🦈🦭🐊🦛🦏🐪🦒🦘🦬🐃🐂🐄🐎",
                        "🐖🐏🦙🐐🦌🐕🦙🦌🐩🦙🐐🐕🦃🦚🐓🦩🐇🦝",
                        "🦨🦡🦦🦥🍃🍂🍄🍄🪨🌾💐🌹🥀🌺🌼🌻🌞🌝🌛🌚"
        ]
        time.sleep(5)
        if(id=="iphone"):
            link="https://www.instagram.com/p/Cb_Qx_bAiRT/"
        elif(id=="big"):
            link="https://www.instagram.com/p/Cb-9wW4Of66/"
        driver.get(link)
        time.sleep(5)
        inicio=time.time()
        fail=0
        tempo=500
        for i in range(600):
            texto=random.choice(comments)
            try:
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 7))
                self.digite_que_nem_gente(texto,comment_input_box)
                time.sleep(random.randint(1, 6))

                driver.find_element_by_xpath("//div[contains(text(),'Post')]/..").click()

                print("Comentou " + id)
                time.sleep(random.randint(2, 4))

            except Exception as e:
                print("\n\nBloqueou!"+id)
                print(e)
                fail=fail+1
                time.sleep(5)
                if(i%10==0):
                    fail=0
                if(fail==3):
                    with open(id+"_Relatório.txt", "a+") as arquivo:
                        arquivo.write("\nComentários bem sucedidos!!  -->  comentou "+str(i)+" vezes no "+id)
                        arquivo.close()
                    break
                self.driblar(link, 45)
            j=i+1
            if(j%20==0):
                final=time.time()
                tempo=(final-inicio)/60
                print("\nTempo da iteração(em minutos): ", tempo)
                print("Número de comentários na iteração: ", i)
            time.sleep(50)

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

    
    def alternative_main(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        self.login(int(sys.argv[1]))
        self.rolar_no_explorar(120)
        for j in range (15):
            try:     
                iteracTotal=0
                tempo0=time.time()
                for i in range(100):
                        numero=4
                        inicio=time.time()
                        iterac=0
                        time.sleep(5)
                        iterac+=self.comente("xre")
                        time.sleep(5)
                        iterac+=self.comente("audi")
                        time.sleep(5)
                        iteracTotal+=iterac
                        final=time.time()
                        tempo=(final-inicio)/60
                        tempoTotal=(final-tempo0)/60
                        print("\nTempo da iteração(em minutos): ", tempo)
                        print("\nTempo do programa(em minutos): ", tempoTotal)
                        print("Número de comentários na iteração: ", iterac)
                        print("Número de comentários no total: ", iteracTotal)
                        if(iterac<numero):
                                print("VAMOS GANHAR !!!")
                                return 0
            except Exception as e:
                print("!!!!  TENTOU SAIR DO PROG ;)  !!!!")
                time.sleep(60)
                pass
            
    def main(self):
        driver = self.driver
        self.login(int(sys.argv[1]))
        self.comente(sys.argv[2])



RachidBot = InstagramBot()
RachidBot.main()

"""
    °°°°INSTRUÇÕES°°°°
1º apertar ctrl+F5
2º Esperar uns 2 minutin pro programa abrir
3º Colocar o próximo número para LOGIN(sequência normal, de 1 a 16
obs: o número a ser alterado é o dentro dos parênteses 
self.login(-->  1  <--)
"""
