import os
import glob
import ntpath
from dirstate.utils import compress, new_state_id, parse_state_id
from dirstate.constants import DIRECTORY


def get_states(directory):
    return filter(
        lambda x: x['directory'] == directory,
        [
            dict(
                parse_state_id(ntpath.basename(fname)), **dict(file=fname)
            )
            for fname in glob.glob(os.path.join(DIRECTORY, '*.tar.gz'))
        ]
    )


def save_state(directory):
    compress(
        os.path.join(DIRECTORY, new_state_id(directory)),
        directory
    )


def set_state(directory, timestamp):
    pass
