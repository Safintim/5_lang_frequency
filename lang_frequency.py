import argparse
import os.path


def create_parser():
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument('file', nargs='?', default=False, help='Path to json file')
    return parser


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text):
    pass


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    if not namespace.file:
        exit('Укажите путь к файлу.')
    if not os.path.isfile(namespace.file):
        exit('Такого файла не существует.')

    text = load_data(namespace.file)
    get_most_frequent_words(text)


if __name__ == '__main__':
    main()
