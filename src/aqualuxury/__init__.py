import argparse

import bs4
import requests

__project_name__ = "aqualuxury"


def extract_image_url(url):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.content, features="html.parser")
    meta = soup.find("meta", attrs={"property": "og:image"})
    return (
        meta.attrs["content"]
        if meta and "content" in meta.attrs
        else "Image URL not found"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract image URLs from Instagram posts."
    )
    parser.add_argument("urls", nargs="+", help="One or more Instagram post URLs")
    args = parser.parse_args()

    for url in args.urls:
        image_url = extract_image_url(url)
        print(f"Original URL: {url}")
        print(f"Image URL: {image_url}")
        print()

    return 0
