# @refs: https://github.com/yaml/pyyaml
import yaml
import sys
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from collections import OrderedDict

"""
" Implements class for handling YAML file format.
"""
class YAMLFormat(yaml.YAMLObject):
    data = None

    def __init__(self, file=None, content=None):
        """
        " Class constructor.
        """
        if file:
            with open(file, 'r') as f:
                content = f.read()
        if content:
            self.load(content)

    def __iter__(self):
        """
        " Makes the object iterable.
        " @fixme: TypeError: iter() returned non-iterator of type 'dict'
        """
        return self.data

    def load(self, data):
        """
        " Parse the first YAML document in a stream,
        " and produce the corresponding Python object.
        """
        self.data = yaml.load(data, Loader=Loader)

    def dump(self, **args):
        """
        " Dumps YAML content.
        " @docs: https://pyyaml.org/wiki/PyYAMLDocumentation
        """
        return yaml.dump(self.data, Dumper=Dumper, **args)

    def parse(self):
        """
        " Parse a YAML stream and produce parsing events.
        """
        return yaml.parse(self.data, Loader=Loader)

    def compose(self):
        """
        " Parse the first YAML document in a stream.
        " and produce the corresponding representation tree.
        """
        return yaml.compose_all(self.data, Loader=Loader)

    @staticmethod
    def map(self):
        """ @see: https://github.com/wimglenn/oyaml """
        _items = 'viewitems' if sys.version_info < (3,) else 'items'
        def map_representer(dumper, data):
            return dumper.represent_dict(getattr(data, _items)())
        def map_constructor(loader, node):
            loader.flatten_mapping(node)
            return OrderedDict(loader.construct_pairs(node))
        yaml.add_representer(dict, map_representer)
        yaml.add_representer(OrderedDict, map_representer)
        yaml.add_representer(dict, map_representer, Dumper=yaml.dumper.SafeDumper)
        yaml.add_representer(OrderedDict, map_representer, Dumper=yaml.dumper.SafeDumper)