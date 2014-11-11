from kao_command.command_list import CommandList

__command_manager__ = None

class CommandManager:
    """ Manages the commands with their list of arguments to determine which command should be run """
    
    def __init__(self, scriptName):
        """ Initialize the Command Manager with the name of the script this is managing commands for """
        self.scriptName = scriptName
        self.rootCommandList = CommandList(scriptName)
        
    def register(self, command, category=None):
        """ Register the given Command """
        if hasattr(command, "category"):
            category = command.category
            
        commandList = self.getCommandListForCategory(category)
        
        commandList.addCommand(command.command, command())
        
    def run(self, args):
        """ Run the command based on the given arguments """
        if len(args) > 0 and args[0] == "-c":
            self.getTabCompletion(args[1:])
        else:
            self.rootCommandList.run(args)
        
    def getTabCompletion(self, arguments):
        """ Get the Tab Completion for the arguments """
        results = self.rootCommandList.getTabCompletion(arguments)
        results.sort()
        print " ".join(results)
        
    def getCommandListForCategory(self, category):
        """ Return the command list for the given category """
        commandList = self.rootCommandList
        if category is not None and category != '':
            for category in category.split('/'):
                if category in commandList:
                    commandList = commandList[category]
                else:
                    newCommandList = CommandList(self.scriptName, category)
                    commandList.addCommand(category, newCommandList)
                    commandList = newCommandList
        return commandList
        
def SetScriptName(scriptName):
    """ Registers a Command with the Command Manager """
    global __command_manager__
    __command_manager__ = CommandManager(scriptName)

def RegisterCommand(command, category=None):
    """ Registers a Command with the Command Manager """
    global __command_manager__
    __command_manager__.register(command, category=category)
    
def Run(arguments):
    """ Run the given Command """
    global __command_manager__
    __command_manager__.run(arguments)