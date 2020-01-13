import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

base_url = 'https://verter.org/xiaomi.html?page=1'


def hh_parse(base_url: object, headers: object):
    product = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', {'class': 'product-thumb'})
        for div in divs:
            title = div.find('h4').text
            href = div.find('a')['href']
            cod_product = div.find('span').text
            price = div.find('p', {'class': 'price'}).text
            stock = div.find('p', {'oct-product-stock'}).text
            product.append({
                'Название товара' : title,
                'Ссылка на товар' : href,
                'Код товара' : cod_product,
                'Цена' : price,
                'Наличие товара' : stock
            })
            print(product)
    else:
        print('Error!!!')


hh_parse(base_url, headers)
