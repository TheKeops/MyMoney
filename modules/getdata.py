# modules/getdata.py

import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_currency_data(currency="Help"):
    if currency == "USD=TRY":
        url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _usd = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        usd = float(_usd.replace(',', '.'))

        return usd
    
    elif currency == "EUR=TRY":
        url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _eur = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        eur = float(_eur.replace(',', '.'))

        return eur
    
    elif currency == "GBP=TRY":
        url = "https://www.google.com/finance/quote/GBP-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _gbp = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        gbp = float(_gbp.replace(',', '.'))

        return gbp
    
    elif currency == "TRY=USD":
        url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _usd = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        usd = float(_usd.replace(',', '.'))
        try:
            trtousd = 1 / usd
            return trtousd
        except ZeroDivisionError:
            print("Error: Division by zero")

    elif currency == "EUR=USD":
        url = "https://www.google.com/finance/quote/EUR-USD?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _eur = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        eur = float(_eur.replace(',', '.'))

        return eur
    elif currency == "GBP=USD":
        url = "https://www.google.com/finance/quote/GBP-USD?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _gbp = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        gbp = float(_gbp.replace(',', '.'))

        return gbp
    elif currency == "USD=EUR":
        url = "https://www.google.com/finance/quote/EUR-USD?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _eur = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        eur = float(_eur.replace(',', '.'))
        try:
            usdtoeur = 1 / eur
            return usdtoeur
        except ZeroDivisionError:
            print("Error: Division by zero")

    elif currency == "GBP=EUR":
        url = "https://www.google.com/finance/quote/GBP-EUR?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _gbp = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        gbp = float(_gbp.replace(',', '.'))

        return gbp

    elif currency == "TRY=EUR":
        url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _eur = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        eur = float(_eur.replace(',', '.'))
        try:
            trtoeur = 1 / eur
            return trtoeur
        except ZeroDivisionError:
            print("Error: Division by zero")

    elif currency == "TRY=GBP":
        url = "https://www.google.com/finance/quote/GBP-TRY?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _gbp = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        gbp = float(_gbp.replace(',', '.'))
        try:
            trtogbp = 1 / gbp
            return trtogbp
        except ZeroDivisionError:
            print("Error: Division by zero")

    elif currency == "EUR=GBP":
        url = "https://www.google.com/finance/quote/GBP-EUR?hl=tr"

        sayfa = requests.get(url)
        html_page = BeautifulSoup(sayfa.content, 'html.parser')
        _gbp = html_page.find('div', class_='YMlKec fxKbKc').get_text()

        gbp = float(_gbp.replace(',', '.'))
        try:
            eurtogbp = 1 / gbp
            return eurtogbp
        except ZeroDivisionError:
            print("Error: Division by zero")
    else:
        if currency == "Help":
            help_text = """
            Available currency conversion options:
            - USD=TRY : US Dollar to Turkish Lira
            - TRY=USD : Turkish Lira to US Dollar
            - EUR=TRY : Euro to Turkish Lira
            - TRY=EUR : Turkish Lira to Euro
            - GBP=TRY : British Pound to Turkish Lira
            - TRY=GBP : Turkish Lira to British Pound
            - EUR=USD : Euro to US Dollar
            - USD=EUR : US Dollar to Euro
            - GBP=USD : British Pound to US Dollar
            - USD=GBP : US Dollar to British Pound
            - EUR=GBP : Euro to British Pound
            - GBP=EUR : British Pound to Euro
            """
            return help_text
        else:
            return "Error: Invalid currency conversion option. Type 'Help' for available options."
        