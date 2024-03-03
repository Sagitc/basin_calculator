import os, requests
from bs4 import BeautifulSoup


def clearTerminal():
    os.system('cls')

def apresentation():
    print('---- Calculadora de Décio Basin ----')

def exitProgram(string):
    if string == "sair" or string == "exit":
        return quit()
    
def dividendYieldAndFairPrice(dividend,actualPrice):
    dividendYield = (dividend/actualPrice)*100
    fairPrice = dividend/(dividendYield/100)
    return dividendYield, fairPrice

def isWorth(actionPrice, fairPrice, selicValue, dividendYield):
    if actionPrice <= fairPrice and dividendYield > selicValue:
        return 'A ação é válida.'
    else:
        return 'A ação não é válida.'


# ---------------------------------------------------- #


print('Seja bem-vindo(a) à calculadora de Décio Basin.')
print('\nCalcularemos o dividend yield e o preço real de uma ação e diremos se a ação é rentável\n\
de acordo com método do Basin.')
print('\n\nAdvertimos ao usuário que esse programa não fornece qualquer tipo de instrução na área \n\
financeira, apenas dá resultados de acordo com os dados que recebe e informa se a ação \n\
é válida ou não sob pretexto dos ensimanentos de Basin.')
print('É de total responsabilidade do usuário o que ele fará com as informações que receber\n\
do programa.')

input('\nSe aceita as declarações acima, pressione qualquer tecla para continuarmos.')

clearTerminal()

while True:
    apresentation()

    URL = ('https://www.google.com/search?q=valor+taxa+selic+atual&client=opera-gx&hs=IHL&sca_esv=19c5bc5ef87e6314&sxsrf=ACQVn09PnF5ZWBl2SS16HN8JqDyFOmCtXA%3A1709432645503&ei=Rd_jZYynHtD11sQP9sCPiAQ&udm=&ved=0ahUKEwjM3ejshNeEAxXQupUCHXbgA0EQ4dUDCBA&uact=5&oq=valor+taxa+selic+atual&gs_lp=Egxnd3Mtd2l6LXNlcnAiFnZhbG9yIHRheGEgc2VsaWMgYXR1YWwyBRAAGIAEMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeSJkJUABYyQdwAHgAkAEAmAGPAaABigaqAQMwLja4AQPIAQD4AQGYAgWgAogFwgIHECMYsAIYJ8ICBxAAGIAEGA3CAgYQABgHGB7CAggQABgIGAcYHsICCBAAGAgYHhgNmAMAkgcDMC41oAfkJg&sclient=gws-wiz-serp')
    headers = { 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    fees = float(soup.find('div', class_ = 'IZ6rdc').get_text().replace(",",".").replace("%",""))

    print(f'A taxa de juros atual é {fees}')
    dividend = float(input('\nInsira o valor do dividendo anual da ação escolhida: ').replace(",","."))
    actionValue = float(input('Insira o valor atual da cota escolhida: ').replace(",","."))

    dividendYield, fairPrice = dividendYieldAndFairPrice(dividend,actionValue)

    print(f'\n\nDividendo Yield => {dividendYield:.2f}%')
    print('Preço justo => %.2f'%fairPrice)

    print()
    print('%s'%isWorth(actionValue, fairPrice, fees, dividendYield))

    answer = input('\n\nClique em qualquer tecla para continuar ou digite "sair" para terminar o programa.')
    if answer == 'sair':
        quit()

    clearTerminal()
