#!/usr/bin/env python3
"Takes an float and returns the string representation of the float."


def to_str(n: float) -> str:
    "Coverts float to string"
    new = format(n, 'f')
    return new
