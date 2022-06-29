"""
read: 336
"""

import argparse
from os import system

TOTAL_PAGES = 711


def main(current_page):

    with open(__file__, 'r') as file:
        lines = file.readlines()

    lines[1] = 'read: {}\n'.format(current_page)

    with open(__file__, 'w') as file:
        for line in lines:
            file.write(line)

    progress = int(current_page) / TOTAL_PAGES * 100

    system('git add -A')
    system('git commit -m "{}"'.format(lines[1]))
    system('git push origin read')

    print('\nCurrent progress: {:.2f}'.format(progress), end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('current_page')
    args = parser.parse_args()
    main(args.current_page)
