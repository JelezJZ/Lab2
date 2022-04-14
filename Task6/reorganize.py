from sys import argv
import os
import argparse
from glob import glob
import pathlib
import time
from typing import Dict
import shutil

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', nargs=1, default=pathlib.Path.cwd(), type=str)
    parser.add_argument('--days', nargs=1, default=0, type=int)
    parser.add_argument('--size', nargs=1, default=0, type=int)
    return parser

if __name__ == '__main__':

    parser = create_parser()
    namespace: argparse.Namespace = parser.parse_args(argv[1:])

    cur_time = int(time.strftime('%j', time.localtime()))

    files: list = glob(f'{namespace.source[0]}\\*.*')
    dates: Dict[str, int] = {file : int(time.strftime('%j', time.gmtime(os.path.getmtime(file)))) for file in files}
    archive: list = [k for k, v in dates.items() if cur_time - v > namespace.days[0]]

    if archive:
        pathlib.Path.mkdir(pathlib.Path.cwd() / 'Archive')
        for src in archive:
            shutil.move(src, pathlib.Path.cwd() / 'Archive')

    files = glob(f'{namespace.source[0]}\\*.*')
    sizes: Dict[str, int] = {file : os.path.getsize(file) for file in files}
    small: list = [k for k, v in sizes.items() if v < namespace.size[0]]

    if small:
        pathlib.Path.mkdir(pathlib.Path.cwd() / 'Small')
        for src in small:
            shutil.move(src, pathlib.Path.cwd() / 'Small')