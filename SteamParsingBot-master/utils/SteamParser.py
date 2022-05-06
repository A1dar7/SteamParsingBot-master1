import aiohttp
import json

# https://steamcommunity.com/market/listings/570/Manifold%20Paradox/render/?query=&start=0&count=100&country=RU&language=russian&currency=5

# https://steamcommunity.com/market/priceoverview/?currency=5&country=RU&appid=570&market_hash_name=Manifold%20Paradox&format=json

# https://community.akamai.steamstatic.com/economy/image/

collect_currency = {
    'USD': 1, 'GBP': 2, 'EUR': 3, 'CHF': 4, 'RUB': 5, 'PLN': 6, 'BRL': 7, 'JPY': 8, 'SEK': 9, 'IDR': 10,
    'MYR': 11, 'PHP': 12, 'SGD': 13, 'THB': 14, 'VND': 15, 'KRW': 16, 'TRY': 17, 'UAH': 18, 'MXN': 19, 'CAD': 20,
    'AUD': 21, 'NZD': 22, 'CNY': 23, 'INR': 24, 'CLP': 25, 'PEN': 26, 'COP': 27, 'ZAR': 28, 'HKD': 29, 'TWD': 30,
    'SAR': 31, 'AED': 32, 'ARS': 34, 'ILS': 35, 'KZT': 37, 'KWD': 38, 'QAR': 39, 'CRC': 40, 'UYU': 41
}


async def collect_data(APP_ID, SLOT_NAME, START=0, COUNT=1, COUNTRY='RU', CURRENCY='RUB'):
    STEAM_IMAGE = 'https://community.akamai.steamstatic.com/economy/image/'
    STEAM = 'https://steamcommunity.com/market/listings'
    QUERY = f'render?query=&start={START}&count={COUNT}&country={COUNTRY}&currency={collect_currency[CURRENCY]}'
    URL = f'{STEAM}/{APP_ID}/{SLOT_NAME}/{QUERY}'

    async with aiohttp.ClientSession() as session:
        res = await session.get(URL)
        pay_cards = list()

        datas = json.loads(await res.text())
        for data in datas['listinginfo']:
            pay_card = dict()
            pay_card['price'] = price_normalize(str(datas['listinginfo'][data]['converted_fee_per_unit']),
                                                str(datas['listinginfo'][data]['converted_price_per_unit']))
            for data in datas['assets'][str(APP_ID)]['2']:
                pay_card['image'] = STEAM_IMAGE + datas['assets'][str(APP_ID)]['2'][data]['icon_url_large']
                pay_card['name'] = datas['assets'][str(APP_ID)]['2'][data]['name']
                pay_card['type'] = datas['assets'][str(APP_ID)]['2'][data]['type']
                pay_card['value'] = datas['assets'][str(APP_ID)]['2'][data]['descriptions'][0]['value']
            pay_cards.append(pay_card)
        return pay_cards


def price_normalize(fee, price, contextid=2):
    fee = fee[:len(fee) - contextid] + '.' + fee[len(fee) - contextid:]
    price = price[:len(price) - contextid] + '.' + price[len(price) - contextid:]

    total_price = float(fee) + float(price)
    if total_price % int(total_price) != 0:
        return round(total_price, 2)
    else:
        return int(total_price)


if __name__ == '__main__':
    collect_data(570, 'Manifold%20Paradox')
