from re import findall
def main():
    file = input("Введите название файла: ")
    files = open(file, 'r', encoding='utf-8')
    text = files.read()
    find_ip: list = findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
    print(find_ip)
    files.close()
if __name__ == "__main__":
    main()