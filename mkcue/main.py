# coding: utf_8
from glob import iglob
from pathlib import Path
import click

T1 = '''\
PERFORMER "PERFORMER"
TITLE "TITLE"\
'''

T2 = '''\
FILE "{}" WAVE
  TRACK {:02d} AUDIO
    INDEX 01 00:00:00\
'''


@click.command()
@click.argument('pattern')
def main(pattern):
    print(T1)
    for i, p in enumerate(map(Path, iglob(pattern)), 1):
        print(T2.format(p.name, i))


if __name__ == '__main__':
    main()
