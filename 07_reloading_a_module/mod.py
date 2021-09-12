s = 'Computers are useless. They can only give you answers'
a = [100, 200, 300]

_should_not_be_imported_with_asterisk = 10

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

# Making the below change after importing
print(f'a = {a}')
# Within this directory of 07_reloading_a_module, if we launch a python3 session and type the following commands, we get the followin results
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 07_reloading_a_module % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod
# >>> # make the change to the mod.py now and import again
# >>> import mod
# >>> # we can see that nothing happened, so we can close and open the interpreter again. Or we can use importlib.reload as below
# >>> import importlib
# >>> importlib.reload(mod)
# a = [100, 200, 300]
# <module 'mod' from '/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/07_reloading_a_module/mod.py'>
