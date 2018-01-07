
import json
from collections import OrderedDict


def load_file(filename, ordered_dict=False):

    with open(filename, 'r') as f:
        lines = f.readlines()
        # drop the first line
        content = ''.join(lines[1:])
        if ordered_dict:
            data = json.loads(content, object_pairs_hook=OrderedDict)
        else:
            data = json.loads(content)
    return data


def load_files(filenames, ordered_dict=False):

    data = []
    for filename in filenames:
        _data = load_file(filename, ordered_dict)
        data.extend(_data)

    return data
