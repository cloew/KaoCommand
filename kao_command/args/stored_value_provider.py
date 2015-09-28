
def StoredValueProvider(name, args):
    """ Return the value from the args """
    return getattr(args, name)