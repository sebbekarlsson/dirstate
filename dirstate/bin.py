import os
import sys
from dirstate.utils import initialize
from dirstate.state import save_state, get_states, set_state


def run():
    initialize()

    path = os.getcwd()

    if sys.argv[1] == 'log':
        print(get_states(path))

    elif sys.argv[1] == 'save':
        print(save_state(path))
    elif sys.argv[1] == 'set':
        print(set_state(path, sys.argv[2]))
