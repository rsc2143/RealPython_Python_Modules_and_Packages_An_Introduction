s = 'Computers are useless. They can only give you answers'
a = [100, 200, 300]

_should_not_be_imported_with_asterisk = 10

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

# Within this directory of 04_the_import_statement, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 04_the_import_statement % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from mod import *
# >>> mod._should_not_be_imported_with_asterisk
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mod' is not defined
# >>> a
# [100, 200, 300]
# >>> printy('a')
# arg = a
# >>> Classy()
# <mod.Classy object at 0x7ff0ee972f50>
# >>> _should_not_be_imported_with_asterisk
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name '_should_not_be_imported_with_asterisk' is not defined
# >>> try:
# ...     # Non existent module
# ...     import foo
# ... except:
# ...     print('foo not found')
# ...
# foo not found
# >>> try:
# ...     # Existing module, but object unavailable
# ...     from mod import bar
# ... except:
# ...     print('object not found')
# ...
# object not found
