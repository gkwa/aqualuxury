class ResultPrinter:
    def print_results(self, results):
        for i, (original_url, image_url) in enumerate(results):
            print(original_url)
            print(image_url)
            if i < len(results) - 1:
                print()
