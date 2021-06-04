import os
from terminal_colors import bcolors


class Quotes:
    def __init__(self):
        self.raid_quotes = []
        self.keys_quotes = []
        self.personalized_quotes = {}

        self.load_quotes()


    def load_file(self, root, file_name):
        file = open(os.path.join(root, file_name), 'r')
        print(f'Load {bcolors.WARNING}{bcolors.BOLD}{file_name}{bcolors.ENDC} quotes:')

        lines = [line.removesuffix('\n') for line in file.readlines()]
        for line in lines:
           print(line)

        print('') 

        return lines

    def load_quotes(self):
        root = r'./quotes/'
        general_quotes = self.load_file(root, 'general.txt')
        self.raid_quotes = general_quotes + self.load_file(root, 'raid.txt')
        self.keys_quotes = general_quotes + self.load_file(root, 'keys.txt')

        for sub_root, _, files in os.walk(root + r'personalized/'):
            for file in files:
                self.personalized_quotes[file[:-4]] = self.load_file(sub_root, file)

        for name in self.personalized_quotes:
            print(f'{bcolors.OKGREEN}{name}:{bcolors.ENDC}')

            for quote in self.personalized_quotes[name]:
                print(quote)

            print('')