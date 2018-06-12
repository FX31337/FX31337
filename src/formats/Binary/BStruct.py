import struct
import datetime

class BStruct():
    _endianness = ''
    _fields = []

    def __init__(self, buf, offset = 0):
        for (name, fmt, *rest) in self._fields:
            field_size = struct.calcsize(fmt)
            val = struct.unpack_from(self._endianness + fmt, buf, offset)

            # Flatten the single-element arrays
            if type(val) is tuple and len(val) == 1:
                val = val[0]

            setattr(self, name, val)

            offset += field_size

    def __str__(self):
        ret = ''

        for (name, _, *fmt) in self._fields:
            val_repr = getattr(self, name)
            # Pretty print the value using the custom formatter.
            if len(fmt):
                pp ,= fmt
                val_repr = pp(self, getattr(self, name))

            ret += '{} = {}\n'.format(name, val_repr)

        return ret

    def get_fields_size(self, spec):
        # Prepend an endianness mark to prevent calcsize to insert padding bytes
        fmt_str = '=' + ''.join(x[1] for x in spec)
        return struct.calcsize(fmt_str)