from . import arg_parser, image_extractor, url_processor

__project_name__ = "aqualuxury"


def main() -> int:
    args = arg_parser.parse_arguments()
    extractor = image_extractor.ImageExtractor()
    processor = url_processor.URLProcessor(extractor)

    for url in args.urls:
        result = processor.process(url)
        print(url)
        print(result)
        print()

    return 0
