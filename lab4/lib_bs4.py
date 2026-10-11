from bs4 import BeautifulSoup
def use_bs4():
    soup = BeautifulSoup("<h1>Привіт світ</h1>", "html.parser")
    print(f"BeautifulSoup: Знайдено заголовок -> {soup.h1.text}")