from services.json_convertor import convert


def main():
    url = input('Enter the url you want the program to analyze: ')
    convert(url=url)

if __name__ == '__main__':
    main()