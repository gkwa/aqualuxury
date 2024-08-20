from . import arg_parser, image_extractor, result_printer, url_processor

__project_name__ = "aqualuxury"


def main() -> int:
    args = arg_parser.parse_arguments()
    extractor = image_extractor.ImageExtractor()
    processor = url_processor.URLProcessor(extractor)
    printer = result_printer.ResultPrinter()

    results = [(url, processor.process(url)) for url in args.urls]
    printer.print_results(results)

    return 0
