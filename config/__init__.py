from utils import paths
import toml

import logging

log = logging.getLogger("config")

__content = dict()

def load():
    global __content

    log.info(f"Load configuration variables from {paths.conf_path}")

    # Try load config from path
    with open(paths.conf_path, "r") as fhandle:
        __content = toml.load(fhandle)
    
def get(key):
    keylist = key.split(".")
    node    = __content

    for k in keylist:
        node = node[k]

    return node

