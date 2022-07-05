import bs4
import requests
from fake_headers import Headers

url = "https://habr.com/ru/all/"

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
date_title_link = []

header = Headers(browser="chrome", os="win", headers=True).generate()

response = requests.get(url, headers=header)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

def web_scraping():
    articles = soup.find_all("article")
    for article in articles:

        # Парсинг заголовка
        title = article.find(class_="tm-article-snippet__title-link").find("span").text

        # Парсинг хабов
        hubs = article.find_all(class_="tm-article-snippet__hubs-item")
        hubs = list(hub.text.strip() for hub in hubs)

        # Парсинг основного текста
        osnova = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        osnova = list(osnov.text.strip() for osnov in osnova)


        # Парсинг даты
        data = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs["title"]

        # Парсинг ссылка
        link = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        link = "https://habr.com" + link

        # Для вывода в консоль о новых статьях
        conclusion = "\n\nДата:  " + data + "\nЗаголовок:  " + title + "\nСсылка:   " + link


        #       Текст preview
        all = title + str(hubs) + str(osnova)


        for KEYWORD in KEYWORDS:
            if KEYWORD in all:
                date_title_link.append(conclusion)

    selection = set(date_title_link)

    for select in selection:
        print(select)


if __name__ == "__main__":
    web_scraping()