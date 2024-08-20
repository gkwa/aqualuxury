from .arg_parser import parse_arguments
from .image_extractor import ImageExtractor
from .url_processor import URLProcessor

__project_name__ = "aqualuxury"


def main() -> int:
    args = parse_arguments()
    extractor = ImageExtractor()
    processor = URLProcessor(extractor)

    for url in args.urls:
        result = processor.process(url)
        print(url)
        print(result)
        print()

    return 0
