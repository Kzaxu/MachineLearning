import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]

def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


def craw_text(url):
    r = requests.get(url)
    return r.text 


def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    html = craw_text(urls[0])
    print(parse(html))