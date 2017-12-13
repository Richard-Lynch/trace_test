#!/usr/local/bin/python3

import subprocess
from pprint import pprint


def readlines(filename, **kwargs):
    lines = subprocess.run(
        args=["xxd", "-l", "100", filename],
        stdout=subprocess.PIPE).stdout.decode().split('\n')
    data = [r for r in lines if r != '']
    return parsedata(data)


def parsedata(data):
    print('in parse')
    rows = [r.split(' ')[:9] for r in data]
    return rows


if __name__ == "__main__":
    rows = readlines('gcc1.trace')
    pprint(rows)
