import re
import os.path
import argparse
from collections import Counter
import termtables as tt


def create_parser():
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument('file', nargs='?', default=False, help='Path to json file')
    return parser


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text):
    text = re.sub(r'[^\s\w]', '', text.lower())
    return Counter(text.split()).most_common(10)


def print_most_frequent_words(frequent_words):
    header = ['words', 'frequency']
    string = tt.to_string(
        frequent_words,
        header=header,
        style=tt.styles.thin_thick,
        alignment='c')
    print(string)


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    if not namespace.file:
        exit('Укажите путь к файлу.')
    if not os.path.isfile(namespace.file):
        exit('Такого файла не существует.')

    text = load_data(namespace.file)
    print_most_frequent_words(get_most_frequent_words(text))


if __name__ == '__main__':
    main()
