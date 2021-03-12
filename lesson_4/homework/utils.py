import datetime
import decimal

import requests


def get_currency_rate(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if resp.status_code != 200:  # Ok
        print('Данные с сайта ЦБ РФ не доступны')
        exit()
    content = resp.content.decode('windows-1251')

    day, month, year = list(map(int, content.split('Date="')[1].split('"', maxsplit=1)[0].split('.')))
    course_date = datetime.date(year, month, day)

    parts = content.split('</Valute><Valute')
    currency_code = '<CharCode>' + currency.upper() + '</CharCode>'
    for part in parts:
        if currency_code in part:
            currency_rate = decimal.Decimal(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
            break
    else:
        currency_rate = None

    return currency_rate, course_date
