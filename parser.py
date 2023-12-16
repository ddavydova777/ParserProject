import requests
from bs4 import BeautifulSoup
def get_page_content(url):   #принимает ссылку и выводит ее содержимое
  response = requests.get(url) # в переменной response содержится ответ от сервера
  if response.status_code == 200:  # 200 - запрос успешен
      return response.content # возвращает содержимое "response"

def parse_classics_page(url):  # получает содержимое страницы и возвращает список книг
  page_content = get_page_content(url) #переменная, в которой содержится содержимое страницы
  if page_content:
      soup = BeautifulSoup(page_content, 'html.parser') #создаем объект soup, который будет содержать всю структурированную информацию о странице, которую получили с помощью pagecontent
      titles = [title.text.strip() for title in soup.select('h3 a')] # извлекаем текст из "а" элементов, содержащихся в h3 и создаем список 
      prices = [price.text.strip() for price in soup.select('p.price_color')] # извлекаем текст из "p" элементов на веб-странице и удаляет ненужные пробелы
      return titles, prices # получаем спимок названий книг и их цены