from random import betavariate
import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SimpleCrawler/1.0)"
}

def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        # Проверяем, что это текст
        content_type = response.headers.get("Content-Type", "")
        if "text" not in content_type:
            print(f"[SKIP] Не текст: {url}")
            return None

        response.encoding = response.apparent_encoding
        return response.text

    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        return None

page_index = 1
for page_id in range(312882+1, 999999):
    if page_index > 100: exit()
    url = f"https://habr.com/ru/articles/{page_id}/"
    html = fetch_page(url)
    if 'Страница устарела, была удалена или не существовала вовсе' in html:
        continue
    else:
        with open(f"./pages/page_{page_index}.txt", "w", encoding="utf-8") as f:
            f.write(html)

        with open('index.txt', 'a', encoding='utf-8') as file:
            file.write(f'{page_index},page_{page_index}.txt,{url}\n')

        with open('urls.txt', 'a', encoding='utf-8') as file:
            file.write(f'{url}\n')

        page_index += 1

    time.sleep(1)

