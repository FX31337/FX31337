"""
" Defines Provider class.
"""
class Provider():
    requires = {"type"}

    def __init__(self, data):
        self.validate(data)

    def validate(self, data):
        for required in self.requires:
            if not required in data:
                raise ValueError("Missing {}".format(required))