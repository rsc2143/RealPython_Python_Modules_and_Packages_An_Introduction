__all__ = ['load_data']
# The __all__ list controls what is imported when import * is specified

def load_data():
    print('load data using mod.load_data()')

class Customer():
    pass

# Within this directory of 10_importing_asterisk_from_a_package, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 10_importing_asterisk_from_a_package % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from pkg.mod1 import *
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'load_data']
# >>> exit()
