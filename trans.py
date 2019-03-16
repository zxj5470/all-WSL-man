#!/usr/bin/env python3
from string import Template
if __name__ == "__main__":
    f = open("catalog.txt",newline = "\n")
    md = open("catalog.md","w",newline = "\n")
    for line in f:
        line=line[:-1]
        current = f'[{line}](files/{line})\n\n'
        md.write(current)
    md.close()
    f.close()
    pass