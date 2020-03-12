 #!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import pickle
import magic

def load_obj(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

def create_path(path):
    if not os.path.exists(path):
        os.mkdir(path)

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def filetype(f):
    return magic.from_file(f).split()[0]
