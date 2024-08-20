import bs4
import requests

__project_name__ = "aqualuxury"


def main() -> int:
    result = requests.get("https://www.instagram.com/p/B2EtjT9hgvG/")
    c = result.content
    soup = bs4.BeautifulSoup(c)
    metas = soup.find_all(attrs={"property": "og:image"})
    print(metas[0].attrs["content"])
    return 0
