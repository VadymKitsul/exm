import requests
from bs4 import BeautifulSoup
import lxml

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-Agent": user}


sessions = requests.Session()
for j in range(1, 50):
    url = "https://kups.club/?page=1"
    response = sessions.get(url, headers=headers)
    # print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        # print(soup)
        products = soup.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
        # print(products[0])

    for prod in products:
        if prod.find('div', class_="card h-100"):
            title = prod.find("h3", class_="card-title")
            price = prod.find("p", class_="card-text")
            try:
                discound_from = prod.find("p", class_="card-text text-black-50 one-line h25px mb-0")
                discound_from = discound_from.text
            except AttributeError:
                discound_from = prod.find("a", class_="text-black link-default").text

            print('Product: ', title.text.strip(), 'price: ', price.text)
            with open("catalog.txt" , "a", encoding='utf-8') as file:
                file.write(f"{title.text} {price.text} {discound_from} \n")
            with open("catalog.exml" , "a", encoding='utf-8') as file:
                file.write(f"{title.text} {price.text} {discound_from} \n")