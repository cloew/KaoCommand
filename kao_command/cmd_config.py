from argparse import ArgumentParser
from kao_modules import NamespacedClass

class CmdConfig:
    """ Represents the configuration for a command """
    
    def __init__(self, argString, classString):
        """ Initialize with the preceeding arguments and the module """
        self.argString = argString
        self.namespacedClass = NamespacedClass(classString)
        
    def run(self, scriptName, args):
        """ Run the Command Config """
        command = self.namespacedClass.instantiate()
        parser = ArgumentParser(prog="{0} {1}".format(scriptName, self.argString))
        command.addArguments(parser)
        arguments = parser.parse_args(argsForNextCommand)
        command.run(arguments)