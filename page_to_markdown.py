import requests
from readability import Document
from html2text import html2text
import argparse
from sys import stdout

parser = argparse.ArgumentParser(
    description="""
Turn a URL into markdown. That's it!
    """,
)
parser.add_argument(
    "url",
    help="The URL of the page",
    type=str
)

if __name__ == '__main__':
    args = parser.parse_args()
    response = requests.get(args.url)
    doc = Document(response.text)
    simplified_markdown = html2text(doc.summary())
    print(simplified_markdown, file=stdout)
