# 4 вариант составьте парсер, который собирает названия книг и цену с первой страницы раздела классической литературы. используйте пакет bs4. http://books.toscrape.com/catalogue/category/books/classics_6/index.html  (минимум две функции)
import requests
# используется для отправки запроса на сервер и получения данных 
from bs4 import BeautifulSoup
# beautifulsoup является частью библиотеки bs4. помогает получать данные с веб-страницы

from parser import parse_classics_page, get_page_content

def main():
    url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'
    page_content = get_page_content(url)
    titles, prices = parse_classics_page(url)
    for title, price in zip(titles, prices):
      print(f"Title: {title}, Price: {price}")

if __name__ == "__main__":
    main()




