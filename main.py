import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
for i in range(1, 10):
    print(f"Page => {i}")
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    url = f"https://rozetka.com.ua/network-adapters/c80196/page={i}"

    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        all_products = soup.find('ul', class_="catalog-grid ng-star-inserted")
        products = all_products.find_all('div', class_="goods-tile__content")

        for b in range(len(products)):
            try:
                title = products[b].find("span", class_="goods-tile__title").text
                oldprice = products[b].find("div", class_="goods-tile__price--old price--gray ng-star-inserted").text
                price = products[b].find("span", class_="goods-tile__price-value").text
                with open("vivod.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} зі старою ціною {oldprice}, та c знижкою {price}\n")
                    title = title.replace(" ", "")
                print(title, oldprice, price)
            except:
                print(f"{title} - Знижки немає.")
