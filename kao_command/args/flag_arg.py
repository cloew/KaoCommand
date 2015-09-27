
class FlagArg:
    """ Represents an Flag Argument for a Command """
    
    def __init__(self, flag, **kwargs):
        """ Initialize the argument with its values """
        self.name = flag.replace('-', '')
        self.argparseHelper = ArgparseHelper(flag, **kwargs)
    
    def addArguments(self, parser):
        """ Add argument to the parser """
        self.argparseHelper.addArg(parser)
        
    def getValue(self, args):
        """ Return the value from the args """
        return getattr(args, self.name)