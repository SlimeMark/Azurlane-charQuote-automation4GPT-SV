import os
import time
import requests
from bs4 import BeautifulSoup

character = ''
language = ''

def quote_language(language):
    if language == 'jp':
        return 'Japanese Server'
    elif language == 'en':
        return 'English Server'
    elif language == 'cn':
        return 'Chinese Server'

def get_quote(character, language):
    quote_list = []
    start_time = time.time()
    try:
        response = requests.get('https://azurlane.koumakan.jp/wiki/' + character + '/Quotes')
        if response.status_code == 200:
            end_time = time.time()
            et = end_time - start_time
            print('\033[92m'+'\033[1m'+'200 OK')
            print('\033[36m'+'\033[1m'+'响应时间: ' + str(et) + ' 秒')
    except requests.exceptions.RequestException as e:
        print('\033[31m'+'\033[31m'+'\033[1m'+'错误: ' + str(response.status_code) + '\n请检查连接并重试')
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.find('article', attrs={'data-title': quote_language(language)})
    if quote:
        tr_without_description = [tr for tr in quote.find_all('tr') if 'Ship Description' not in tr.text]

    for tr in tr_without_description:
        td_list = tr.find_all('td')
        span_list = [td.find_all('span') for td in td_list]
        for span in span_list:
            for quote in span:
                quote_list.append(quote.text)

    return quote_list