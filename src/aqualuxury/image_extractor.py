import bs4
import requests


class ImageExtractor:
    def extract(self, url):
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.content, features="html.parser")
        meta = soup.find("meta", attrs={"property": "og:image"})
        return (
            meta.attrs["content"]
            if meta and "content" in meta.attrs
            else "Image URL not found"
        )
