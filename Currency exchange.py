import requests
from bs4 import BeautifulSoup

#Euros

#Parsing the Web for the current exchange rate of Euros
europage = requests.get('https://www.exchange-rates.org/Rate/USD/EUR')
eurosoup = BeautifulSoup(europage.content, 'html.parser')
Euro = eurosoup.find(id="ratesTable")



euros = (Euro.find(class_="text-nowrap text-narrow-screen-wrap result").get_text())
#Converting the string to a float so that it can be used in math funtions
euroexc = float(euros[0:6])

#Getting input from the user and preforming the conversion
def EuroConversion():
    print("The current exchange rate for 1 US dollar is : " + euros)
    us_dollars = input("How many US dollars would you like to exchange: ")
    if us_dollars.isdigit():
        us_dollars = float(us_dollars)
        UStoEuro = us_dollars * euroexc
        print(UStoEuro)
    else:
        print("Not a number. Please try again.")
        EuroConversion()




#YEN

yenpage = requests.get('https://www.exchange-rates.org/Rate/USD/JPY')
yensoup =BeautifulSoup(yenpage.content, 'html.parser')
Yen = yensoup.find(id="ratesTable")


yen = (Yen.find(class_="text-nowrap text-narrow-screen-wrap result").get_text())
#print(yen)
yenexc = float(yen[0:7])
#print(yenexc)


def YenConversion():
    print("The current exchange rate for 1 US dollar is :"+yen)
    us_dollars = input("How many us dollars would you like to exchange:")
    if us_dollars.isdigit():
        us_dollars = float(us_dollars)
        UStoYen = us_dollars * yenexc
        print(UStoYen)
    else:
        print("Not a number, please try again.")
        YenConversion()
#Canada

canpage = requests.get('https://www.exchange-rates.org/Rate/USD/CAD')
cansoup = BeautifulSoup(canpage.content, 'html.parser')
Can = cansoup.find(id="ratesTable")


can = (Can.find(class_="text-nowrap text-narrow-screen-wrap result").get_text())
#Converting the string to a float so that it can be used in math funtions
Canexc = float(can[0:6])

#Getting input from the user and preforming the conversion
def CanConversion():
    print("The current exchange rate for 1 US dollar is : " + can)
    us_dollars = input("How many US dollars would you like to exchange: ")
    if us_dollars.isdigit():
        us_dollars = float(us_dollars)
        UStoCan = us_dollars * Canexc
        print(UStoCan)
    else:
        print("Not a number, please try again.")
        CanConversion()


#Gold
def GoldConversion():
    goldpage = requests.get('https://markets.businessinsider.com/commodities/gold-price')
    goldsoup = BeautifulSoup(goldpage.content, 'html.parser')
    Gold = goldsoup.find(class_="price-section__values")

    gold = (Gold.find(class_="price-section__current-value").get_text())
    Goldexc = float(gold[0:10])

    print("The current exchange rate for Gold is " +gold+ " US dollars per ounce.")
    us_dollars = input("How many US dollars would you like to exchange: ")
    if us_dollars.isdigit():
        us_dollars = float(us_dollars)
        UStoGold = us_dollars / Goldexc
        goldounces = str(UStoGold)
        print("You can get " +goldounces+" ounces of gold.")
    else:
        print("Not a number, please try again.")
        GoldConversion()



    
def currencyconverter():
    currencychoice = input("Which currency would you like to exchange \nUS dollars into:(Gold, Euros, Canadian, or Yen): ")
    if currencychoice == "Euros":
        EuroConversion()
        return
    if currencychoice == "Yen":
        YenConversion()
        return
    if currencychoice == "Canadian":
        CanConversion()
        return
    if currencychoice =="Gold":
        GoldConversion()
        return
    else:
        print("Sorry I am a unable to convert your currency to whatever that is!")
        currencyconverter()

currencyconverter()
print("Thank You")

