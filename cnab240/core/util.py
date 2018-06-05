import collections

def merge(original, novo):
    _keys = original.keys()
    for _key in _keys:
        original[_key] = str(novo[_key])
    
    return original