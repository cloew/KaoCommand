from .argparse_helper import ArgparseHelper

class Arg:
    """ Represents an Argument for a Command """
    
    def __init__(self, name, **kwargs):
        """ Initialize the argument with its values """
        self.name = name
        self.argparseHelper = ArgparseHelper(name, **kwargs)
    
    def addArguments(self, parser):
        """ Add argument to the parser """
        self.argparseHelper.addArg(parser)
        
    def getValue(self, args):
        """ Return the value from the args """
        return getattr(args, self.name)