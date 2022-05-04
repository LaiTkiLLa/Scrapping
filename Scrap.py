import requests
import bs4

url = 'https://habr.com/ru'

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Научно-популярное', 'Информационная безопасность',
            'Обработка', 'Физика', 'PostgreSQL','Блог компании Southbridge', 'Модель', 'Будущее здесь']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url,headers=headers)

soup = bs4.BeautifulSoup(response.text, features ='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    for hub in hubs:
        hub = hub.text.strip()
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        time = article.find('time').text
        name = article.find('h2').text
        href = href.replace('/ru', '')
    for key in KEYWORDS:
        if key in hub:
            print(f'Статья была опубликована {time}, название статьи {name}, ссылка на статью {url}{href}')

    ################# Доп задание

    new_url = url + href
    new_response = requests.get(new_url, headers=headers)
    new_soup = bs4.BeautifulSoup(new_response.text, features='html.parser')
    new_articles = new_soup.find_all('article')
    for new_article in new_articles:
        new_article = new_article.text.strip()
    for new_key in KEYWORDS:
        if new_key in new_article:
            print(f'Слово {new_key} упомянулось в статье {new_url}')



