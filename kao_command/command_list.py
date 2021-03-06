from kao_decorators import proxy_for
import argparse

@proxy_for('commands', ['__getitem__', '__len__', '__contains__'])
class CommandList:
    """ Represents a Command that allows access to other Commands """
    
    def __init__(self, commands, argString=''):
        """ Initialize the Command List """
        self.commands = commands
        self.argString = argString
        
    def run(self, scriptName, args):
        """ Run the command list """
        if len(args) > 0 and args[0] in self:
            command = self.commands[args[0]]
            command.run(scriptName, args[1:])
        elif None in self.commands:
            command = self.commands[None]
            command.run(scriptName, args)
        else:
            self.help()
        
    def help(self):
        """ Print the usage for the Command List """
        print("Available {0}".format(self.category))
        commandList = sorted(list(self.commands.keys()))
        for command in commandList:
            print("    {0:<15}{1}".format(command+":", self.commands[command].description))
        
    @property
    def name(self):
        """ Return the name of the Command List """
        args = self.argString.split()
        name = args[-1] if len(args) > 0 else ''
        return name.capitalize()
        
    @property
    def description(self):
        """ Return the description for the Command List """
        return "List of {0}".format(self.category)
        
    @property
    def category(self):
        """ Return the Category name for this List """
        if len(self.name) > 0:
            return "{0} Commands".format(self.name)
        else:
            return "Commands"