from .command_list import CommandList

class Driver:
    """ Runs the commands for this cli application """
    
    def __init__(self, scriptName, commands):
        """ Initialize the Driver with the script name and the commands """
        self.scriptName = scriptName
        self.rootCommandList = commands.build()
        
    def run(self, args):
        """ Run the command based on the given arguments """
        self.rootCommandList.run(self.scriptName, args)