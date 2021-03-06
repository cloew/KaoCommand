from .argparse_helper import ArgparseHelper
from .stored_value_provider import StoredValueProvider

class Arg:
    """ Represents an Argument for a Command """
    
    def __init__(self, name, provider=StoredValueProvider, **kwargs):
        """ Initialize the argument with its values """
        self.name = name
        self.provider = provider
        self.argparseHelper = ArgparseHelper(name, **kwargs)
    
    def addArguments(self, parser):
        """ Add argument to the parser """
        self.argparseHelper.addArg(parser)
        
    def getPair(self, args):
        """ Return the Keyword pair """
        return self.name, self.getValue(args)
        
    def getValue(self, args):
        """ Return the value from the args """
        return self.provider(self.name, args)