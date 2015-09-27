
class ArgparseHelper:
    """ Helper to add an argument to an Argparse parser """
    
    def __init__(self, *args, **kwargs):
        """ Initialize the Argparse Helper """
        self.args = args
        self.kwargs = kwargs
        
    def addArg(self, parser):
        """ Add Arg to the parser """
        parser.add_argument(*self.args, **self.kwargs)