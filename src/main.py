import requests
from bs4 import BeautifulSoup

def main():
    URL = "PLACE YOUR URL HERE"

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="")

    print(len(elements))


if __name__ == "__main__":
    main()