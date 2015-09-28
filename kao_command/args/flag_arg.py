from .argparse_helper import ArgparseHelper
from .stored_value_provider import StoredValueProvider

class FlagArg:
    """ Represents an Flag Argument for a Command """
    
    def __init__(self, shortFlag, longFlag=None, provider=StoredValueProvider, **kwargs):
        """ Initialize the argument with its values """
        flag = longFlag if longFlag is not None else shortFlag
        args = [shortFlag, longFlag] if longFlag is not None else [shortFlag]
        self.provider = provider
        self.name = flag.replace('-', '')
        
        self.argparseHelper = ArgparseHelper(*args, **kwargs)
    
    def addArguments(self, parser):
        """ Add argument to the parser """
        self.argparseHelper.addArg(parser)
        
    def getPair(self, args):
        """ Return the Keyword pair """
        return self.name, self.getValue(args)
        
    def getValue(self, args):
        """ Return the value from the args """
        return self.provider(self.name, args)