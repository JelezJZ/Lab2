from distutils.filelist import findall
import re
def main():
    text = input("Введите строку: ")
    pattern = '[A-Z][a-z]+[0-9]{2,4}'
    print(re.findall(pattern, text))
if __name__ == "__main__":
    main()