#!python

""" Habit tracker written in python 3.6
"""

import argparse

def parse_args():
    """Parses arguments
    params:

    returns:

    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'mode',
        help='''
        Determines which other bits to call. Try NEW for new habit, DONE
        for done habits today
        ''',
        metavar='SWITCH',
        action=store,
        type=str,
        default=None,
        dest='long arg'
    )



    return parser.parse_args()


def main():
    """docstring for main
    params:

    returns:

    """
    args = parse_args()

    return



if __name__ == '__main__':
    main()
