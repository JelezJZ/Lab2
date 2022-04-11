def main():
    f = open('Task1.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
    ignore_symbol = '""''()/\;:<>.,!@#$%^&* -=+|`~{}[]\n'
    dic = {x.lower(): 0 for _, x in enumerate(text) if x not in ignore_symbol}
    for index, sum in enumerate(text):
        if sum in dic:
            dic[sum] += 1
    global sorted
    sorted = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
    print(sorted)
if __name__ == "__main__":
    main()