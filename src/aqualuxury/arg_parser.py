import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Extract image URLs from Instagram posts."
    )
    parser.add_argument("urls", nargs="+", help="One or more Instagram post URLs")
    return parser.parse_args()
