from .stored_value_provider import StoredValueProvider

def BareWords(name, args):
    """ Return the args as a joined string """
    words = StoredValueProvider(name, args)
    return " ".join(words)