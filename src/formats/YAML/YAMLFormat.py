# @refs: https://github.com/yaml/pyyaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class YAMLFormat():
    data = None

    def __init__(self, file=None, content=None):
        if file:
            with open(file, 'r') as f:
                content = f.read()
        self.load(content)

    def load(self, data):
        self.data = load(data, Loader=Loader)

    def dump(self):
        return dump(self.data, Dumper=Dumper)