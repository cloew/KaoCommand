from distutils.core import setup

setup(name='kao_command',
      version='0.3.0',
      #description='Kao Tessur Command Framework',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_command', 'kao_command.args'],
      requires=['argparse', 'kao_modules', 'kao_decorators']
     )