from .BStruct import BStruct

class TicksRaw(BStruct):
    _endianness = '<'
    _fields = [
            ('time', 'I'),
            ('bid', 'd'),
            ('ask', 'd'),
            ]
    _size = BStruct.get_fields_size(BStruct, _fields)
    assert(_size == 40)