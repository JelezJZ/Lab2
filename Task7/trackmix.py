from ast import parse
from cmath import log
import ffmpeg
import os
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', required=True)
    parser.add_argument('--destination', '-d', default='mix.mp3')
    parser.add_argument('--count', '-c', default=-1)
    parser.add_argument('--frame', '-f', default=10)
    parser.add_argument('--log', '-l', action='store_const', const=True)
    return parser

def main():
    parser = createParser()
    namespace = parser.parse_args()

    path = namespace.source
    destination = namespace.destination
    count = namespace.count
    frame = namespace.frame
    log = True if namespace.log else False

    files_list = [path for path in os.listdir(
        path) if not os.path.isdir(path) and os.path.splitext(path)[1] == ".mp3"]

    counter = 1
    count = len(files_list) if count != -1 else count
    cuts_file_path_list = []
    for file in files_list:
        name = f'cut{counter}.mp3'
        cuts_file_path_list.append(f'./{name}')
        ffmpeg.input(os.path.join(path, file)).filter('atrim', duration=frame).output(
            f'{name}').run()
        if log:
            print(f'------- processing file {counter} :{path}')
        counter += 1
        count -= 1
        if count == 0:
            break

    with open('list.txt', 'w+') as f:
        for path in cuts_file_path_list:
            f.write(f'file {path} \n')

    os.system(
        f'ffmpeg -f concat -safe 0  -i list.txt -codec copy {destination}')

    for path in cuts_file_path_list:
        os.remove(path)

    os.remove('./list.txt')

if __name__ == '__main__':
    main()