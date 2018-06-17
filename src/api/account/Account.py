"""
" Implements Account class.
"""
class Account():
    requires = {"provider"}

    def __init__(self, data):
        for required in self.requires:
            if not required in data:
                raise ValueError("Missing {}".format(required))

    def __str__(self):
        pass