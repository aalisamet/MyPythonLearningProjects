import requests as request
from bs4 import BeautifulSoup

url_set =set({})

def crawl(url):
    response = request.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        for link in soup.find_all("a"):
            value = link.get("href")

            if value.__contains__("https://") and not url_set.__contains__(str(value)):
                print(value)
                url_set.add(str(value))
                crawl(value)


if __name__ == "__main__":

    target_url = "https://atilsamancioglu.com"



    crawl(target_url)