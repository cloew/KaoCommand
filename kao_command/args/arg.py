
class Arg:
    """ Represents an Argument for a Command """
    
    def __init__(self, name, **kwargs):
        """ Initialize the argument with its values """
        self.name = name
        self.kwargs = kwargs
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument(self.name, **self.kwargs)
        
    def getValue(self, args):
        """ Return the value from the args """
        return getattr(args, self.name)