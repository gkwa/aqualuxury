class URLProcessor:
    def __init__(self, extractor):
        self.extractor = extractor

    def process(self, url):
        return self.extractor.extract(url)
