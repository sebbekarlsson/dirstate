import os
import sys
import argparse
from dirstate.utils import initialize
from dirstate.state import save_state, get_states


parser = argparse.ArgumentParser()
parser.add_argument(
    'command',
    type=str,
    help='what to do'
)

args = parser.parse_args()


def run():
    initialize()

    path = os.getcwd()

    if sys.argv[1] == 'log':
        print(get_states(path))

    elif sys.argv[1] == 'save':
        print(save_state(path))
    elif sys.argv[1] == 'set':
        pass
