import os
import pytube
import sys

def validate_args(args):
    if len(args) < 2:
        print('The provided arguments are not enough')
        return False

    return True


def get_links(path):
    links = []

    with open(f'{path}', 'r') as file:        
        for link in file.readlines():
            links.append(link.replace('\n', ''))

    return links   


def download(link):
    pass


def main():

    args = sys.argv
    if not validate_args(args): return
    input = args[1]

    links = get_links(input)
    print(links)

    for link in links:
        download(link)


if __name__ == '__main__':
    main()