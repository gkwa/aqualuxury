import json
import re

import bs4
import requests


class ImageExtractor:
    def extract(self, url):
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.content, "html.parser")

        # Try to find the shared data JSON
        shared_data = re.search(r"window._sharedData = (.+);</script>", str(soup))
        if shared_data:
            data = json.loads(shared_data.group(1))
            try:
                post_data = data["entry_data"]["PostPage"][0]["graphql"][
                    "shortcode_media"
                ]
                if "edge_sidecar_to_children" in post_data:
                    # Multiple images
                    return [
                        edge["node"]["display_url"]
                        for edge in post_data["edge_sidecar_to_children"]["edges"]
                    ]
                else:
                    # Single image
                    return [post_data["display_url"]]
            except KeyError:
                pass  # JSON structure not as expected

        # Fallback to og:image if shared data parsing fails
        og_image = soup.find("meta", property="og:image")
        if og_image:
            return [og_image["content"]]

        return ["Image URL not found"]
