__author__ = 'ephemere'


class Manager:

    def __init__(self, form=None):
        if form is None:
            self.keywords = [[]]
        elif not type(form) is list:
            raise Exception
        else:
            self.keywords = form

    def add_keyword(self, font, keywords):
        if not type(keywords) is list:
            keywords = [keywords]

        font = font.lower()
        keywords = [y.lower() for y in keywords]

        for word in keywords:
            if word in self.keywords[0]:
                index = self.keywords[0].index(word)
                if font not in self.keywords[index + 1]:
                    self.keywords[index + 1].append(font)
            else:
                self.keywords[0].append(word)
                self.keywords.append([font])

    def find_fonts(self, keywords):
        if not type(keywords) is list:
            keywords = [keywords]

        keywords = [y.lower() for y in keywords]

        if set(keywords).issubset(set(self.keywords[0])):
            fonts_list = []
            for word in keywords:
                index = self.keywords[0].index(word)
                fonts_list.append(set(self.keywords[index + 1]))
            fonts_list = list(set.intersection(*fonts_list))
            fonts_list = sorted(fonts_list)
        else:
            fonts_list = False
        return fonts_list

    def get_fonts_list(self):
        fonts_list = []
        for i in range(1, len(self.keywords), 1):
            fonts_list.append(set(self.keywords[i]))
        if len(fonts_list) > 0:
            fonts_list = list(set.union(*fonts_list))
            fonts_list = sorted(fonts_list)
        else:
            fonts_list = []
        return fonts_list

    def get_keywords_list(self):
        return sorted(self.keywords[0])

    def _remove_(self, font=None, keyword=None):
        if keyword is not None and font is None and keyword in self.keywords[0]:
            index = self.keywords[0].index(keyword)
            del self.keywords[0][index]
            del self.keywords[index + 1]
        elif font is not None and keyword is None:
            for i in range(1, len(self.keywords)):
                if font in self.keywords[i]:
                    index = self.keywords[i].index(font)
                    del self.keywords[i][index]
        elif font is not None and keyword is not None and keyword in self.keywords[0]:
            index = self.keywords[0].index(keyword)
            if font in self.keywords[index + 1]:
                i = self.keywords[index + 1].index(font)
                del self.keywords[index + 1][i]
        for i in range(len(self.keywords)-1, 0, -1):
                if not self.keywords[i]:
                    del self.keywords[i]
                    del self.keywords[0][i-1]

    def remove(self, font=None, keyword=None):
        if font is not None and type(font) is not list:
            font = [font]
        if keyword is not None and type(keyword) is not list:
            keyword = [keyword]
        if font is None and keyword is not None:
            keyword = [y.lower() for y in keyword]
            for z in keyword:
                self._remove_(keyword=z)
        elif keyword is None and font is not None:
            font = [y.lower() for y in font]
            for z in font:
                self._remove_(font=z)
        else:
            keyword = [y.lower() for y in keyword]
            font = [y.lower() for y in font]
            for z in font:
                for y in keyword:
                    self._remove_(font=z, keyword=y)

    def get_list_form(self):
        return self.keywords

import argparse
from sys import platform as _platform
import os
import os.path
import pickle

parser = argparse.ArgumentParser(description='Simple font manager using keywords.')
subparsers = parser.add_subparsers(dest='subparser', help='valid commands')

parser_add = subparsers.add_parser('add', help='add a connection between a font and one or several keywords')
parser_add.add_argument('font_name', type=str, help='font name here (if it contains spaces use quotes)')
parser_add.add_argument('keyword', type=str, nargs='+', help='keyword here (if it contains spaces use quotes)')

parser_search = subparsers.add_parser('search', help='search for fonts with the specified keyword(s)')
parser_search.add_argument('keyword', type=str, nargs='+', help='keyword here (if it contains spaces use quotes)')

parser_list = subparsers.add_parser('list', help='list all keywords or fonts')
group_list = parser_list.add_mutually_exclusive_group()
group_list.add_argument('-k', '--keyword', action='store_true', help='flag to list keywords')
group_list.add_argument('-f', '--font', action='store_true', help='flag to list fonts')

parser_remove = subparsers.add_parser('remove', help='remove a font or key or a specific connection')
parser_remove.add_argument('-k', '--keyword', type=str, nargs='+', default=None,
                           help='keyword here (if it contains spaces use quotes)')
parser_remove.add_argument('-f', '--font', type=str, nargs='+', default=None,
                           help='font name here (if it contains spaces use quotes)')

args = parser.parse_args()

if _platform == 'linux' or _platform == 'linux2' or _platform == 'darwin':
    path = os.getenv('HOME')
elif _platform == 'win32':
    path = os.getenv('APPDATA')
    #path = os.path.join(path, 'Roaming')
else:
    path = ''

path = os.path.join(path, '.font_keyword_manager')
if not os.path.exists(path):
    os.makedirs(path)
path = os.path.join(path, 'font_manager.data')

if os.path.isfile(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    manager = Manager(data)
else:
    manager = Manager()

if args.subparser == 'add':
    manager.add_keyword(args.font_name, args.keyword)
elif args.subparser == 'search':
    fonts = manager.find_fonts(args.keyword)
    for x in fonts:
        print(x)
elif args.subparser == 'list':
    if args.keyword:
        terms = manager.get_keywords_list()
    else:
        terms = manager.get_fonts_list()
    for x in terms:
        print(x)
elif args.subparser == 'remove':
    manager.remove(args.font, args.keyword)

data = manager.get_list_form()
with open(path, 'wb') as f:
    pickle.dump(data, f)
