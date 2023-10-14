import requests
from bs4 import BeautifulSoup

def last_news():
    url = "https://tengrinews.kz/weather/semey/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Семее: ' + weather_info
    return pagodka

def news():
    url = "https://tengrinews.kz/tag/%D1%81%D0%B5%D0%BC%D0%B5%D0%B9/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    weather_block = soup.find('span', class_="tn-hidden")
    weather_info = weather_block.get_text().strip()
    pagodka = 'Последние новости в Семее:\n' + weather_info
    return pagodka