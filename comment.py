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
giveaway_list = [
    "iphone", "gomez", "gustavo", "bruno", "ilan", "motovlog"
]

class Comment(InstaBot):
    def __init__(self):
        super().__init__()

    def get_link(self, id):
        driver = self.driver
        time.sleep(5)
        dict = self.giveaway_data(id)
        time.sleep(1)
        return dict["link"]

    def comment(self):
        driver = self.driver
        texto=random.choice(comments)
        try:
            comment_input_box = driver.find_element_by_class_name("Ypffh")
            comment_input_box.click()
            
            time.sleep(random.randint(2, 7))
            self.digite_que_nem_gente(texto,comment_input_box)
            time.sleep(random.randint(1, 6))

            driver.find_element_by_xpath("//div[contains(text(),'Post')]/..").click()

            print("Comentou " + id)
            time.sleep(random.randint(2, 4))
            time.sleep(5)
            
            text = driver.find_element_by_xpath("//*[@aria-label='Add a comment…']").text
            if text == texto:
                raise Exception("Ops! Tio Marks parou de enviar o comentário!")


        except Exception as e:
            print("\n\nBloqueou!"+id)
            print(e)

    def comment_loop(self, id):
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
        
        inicio=time.time()
        fail=0
        tempo=500

        self.rolar_no_explorar(30)
        link = self.get_link(id)
        driver.get(link)
        time.sleep(10)

        for i in range(600):
            texto=random.choice(comments)
            try:
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                comment_input_box.click()
                
                time.sleep(random.randint(2, 7))
                self.digite_que_nem_gente(texto,comment_input_box)
                time.sleep(random.randint(1, 6))

                driver.find_element_by_xpath("//div[contains(text(),'Post')]/..").click()

                print("Comentou " + id)
                time.sleep(random.randint(2, 4))
                time.sleep(5)
                
                text = driver.find_element_by_xpath("//*[@aria-label='Add a comment…']").text
                if text == texto:
                    raise Exception("Ops! Tio Marks parou de enviar o comentário!")


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
            j=i+1
            if(j%20==0):
                final=time.time()
                tempo=(final-inicio)/60
                print("\nTempo da iteração(em minutos): ", tempo)
                print("Número de comentários na iteração: ", i)
            time.sleep(50)


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
                        inicio=time.time()
                        iterac=0
                        time.sleep(5)
                        iterac+=self.comment("xre")
                        time.sleep(5)
                        iterac+=self.comment("audi")
                        time.sleep(5)
                        iteracTotal+=iterac
                        final=time.time()
                        tempo=(final-inicio)/60
                        tempoTotal=(final-tempo0)/60
                        print("\nTempo da iteração(em minutos): ", tempo)
                        print("\nTempo do programa(em minutos): ", tempoTotal)
                        print("Número de comentários na iteração: ", iterac)
                        print("Número de comentários no total: ", iteracTotal)
                        if(iterac < len(giveaway_list)*3):
                                print("VAMOS GANHAR !!!")
                                return 0
            except Exception as e:
                print("!!!!  TENTOU SAIR DO PROG ;)  !!!!")
                time.sleep(60)
                pass
            
    def main(self):
        self.login(int(sys.argv[1]))
        self.comment_loop(sys.argv[2])


comment = Comment()
comment.main()
comment.sair()
