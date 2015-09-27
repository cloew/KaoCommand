from .argparse_helper import ArgparseHelper

class FlagArg:
    """ Represents an Flag Argument for a Command """
    
    def __init__(self, shortFlag, longFlag=None, **kwargs):
        """ Initialize the argument with its values """
        flag = longFlag if longFlag is not None else shortFlag
        args = [shortFlag, longFlag] if longFlag is not None else [shortFlag]
        self.name = flag.replace('-', '')
        
        self.argparseHelper = ArgparseHelper(*args, **kwargs)
    
    def addArguments(self, parser):
        """ Add argument to the parser """
        self.argparseHelper.addArg(parser)
        
    def getValue(self, args):
        """ Return the value from the args """
        return getattr(args, self.name)