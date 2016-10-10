# coding=utf-8
import glob
import os

import re

from bs4 import BeautifulSoup


def search(lines, regex):
    for line in lines:
        match = re.search(regex, line)
        if match:
            return line


def get_color(lines, color='#0000ff'):
    regex = '\.(ft\d+){font-style.+color:.*' + color + ';}'
    color_line = search(lines, color)
    if color_line:
        match = re.search(regex, color_line)
        if match:
            return match.group(1)


path = "html"
for filename in glob.glob(os.path.join(path, 'pg_*.htm')):
    colors = []
    soup = BeautifulSoup(open(filename), 'lxml')
    for found in soup.find_all('style'):
        color_code = get_color(found.text.split('\n'))
        if color_code:
            colors.append(color_code)

    if colors:
        print "Page: %0.0f" % int(os.path.basename(filename).strip('pg_').strip('.htm'))
        for color in colors:
            for found in soup.find_all('span', attrs={"class": color}):
                print found.text

        print
