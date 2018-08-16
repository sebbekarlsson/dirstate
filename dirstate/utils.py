import tarfile
import datetime
import base64
import os
import ntpath
from dirstate.constants import STATE_DELIMETER, DIRECTORY


def initialize():
    if not os.path.isdir(DIRECTORY):
        os.mkdir(DIRECTORY)


def compress(filename, directory):
    with tarfile.open(filename + '.tar.gz', mode='w:gz') as archive:
        archive.add(
            directory,
            ntpath.basename(directory),
            recursive=True
        )
    archive.close()

    return archive


def decompress(filename):
    pass


def new_timestamp():
    return int(datetime.datetime.now().strftime('%s'))


def new_state_id(directory):
    return base64.b64encode(
        '{}{}{}'.format(directory, STATE_DELIMETER, new_timestamp())
    )


def parse_state_id(state_id):
    parts = base64.b64decode(state_id).split(STATE_DELIMETER)

    return {
        'directory': parts[0],
        'timestamp': parts[1]
    }
