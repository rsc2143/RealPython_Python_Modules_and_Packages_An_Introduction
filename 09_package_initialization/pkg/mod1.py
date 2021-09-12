def load_data():
    print('load data using mod.load_data()')
    from pkg import alist
    print(f'This is from pkg - {alist}')

class Customer():
    pass

# Within this directory of 09_package_initialization, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 09_package_initialization % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pkg.mod1
# Invoking __init__.py for pkg
# >>> mod1.load_data()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mod1' is not defined
# >>> mod1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mod1' is not defined
# >>> pkg.mod1.
# pkg.mod1.Customer(   pkg.mod1.load_data(
# >>> pkg.mod1.load_data()
# load data using mod.load_data()
# This is from pkg - ['spam', 'bacon', 'eggs']
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 09_package_initialization % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pkg
# Invoking __init__.py for pkg
# >>> pkg.
# pkg.alist  pkg.mod1   pkg.mod2   pkg.pkg
# >>> pkg.mod1
# pkg.mod1
# >>> pkg.mod1.
# pkg.mod1.Customer(   pkg.mod1.load_data(
# >>> pkg.mod1.Customer()
# <pkg.mod1.Customer object at 0x7fca18bb3d90>
# >>> exit()
