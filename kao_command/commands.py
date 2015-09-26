from .cmd_config import CmdConfig
from .command_list import CommandList

class Commands:
    """ Helper class to facilitate easy specification of Commands """
    
    def __init__(self, rootPackage, commandTree):
        """ Initialize with the Root Package the Commands are specified relative to and the Command Tree """
        self.rootPackage = rootPackage
        self.commandTree = commandTree
        
    def build(self):
        """ Build the root Command List """
        return self.buildCommandList([], self.commandTree)
        
    def buildCommandList(self, args, commandTree):
        """ Return the Command List for the Command Tree """
        commands = {}
        for arg, value in commandTree.items():
            newArgs = args + [arg]
            if type(value) == str:
                commands[arg] = CmdConfig(" ".join(newArgs), "{0}.{1}".format(self.rootPackage, value))
            else:
                commands[arg] = self.buildCommandList(newArgs, value)
                
        return CommandList(commands, argString=" ".join(args))