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
        
        for arg in command.args:
            arg.addArguments(parser)
        argResults = parser.parse_args(args)
        
        kwargs = {arg.name: arg.getValue(argResults) for arg in command.args}
        command.run(**kwargs)
        
    @property
    def description(self):
        """ Return the underlying Command's description """
        return self.namespacedClass.cls.description