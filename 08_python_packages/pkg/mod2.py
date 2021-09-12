def clean_data():
    print('cleaning data using mod2.clean_data()')

class Location:
    pass

# Within this directory of 08_python_packages, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 08_python_packages % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pkg
# >>> import importlib
# >>> importlib.reload(pkg.mod1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'pkg' has no attribute 'mod1'
# >>> import pkg.mod1
# >>> pkg.mod1.load_data()
# load data using mod.load_data()
# >>> import pkg.mod2
# >>> pkg.mod2.clean_data()
# cleaning data using mod2.clean_data()
# >>> import pkg.mod1,pkg.mod2
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 08_python_packages % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pkg.mod1,pkg.mod2
# >>> pkg.mod2.Location()
# <pkg.mod2.Location object at 0x7fbd76b78f90>
# >>> pkg.mod1.
# pkg.mod1.Customer(   pkg.mod1.load_data(
# >>> pkg.mod1.Customer()
# <pkg.mod1.Customer object at 0x7fbd76b86610>
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 08_python_packages % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from pkg import mod1
# >>> from pkg import mod2
# >>> mod1.
# mod1.Customer(   mod1.load_data(
# >>> mod1.Customer()
# <pkg.mod1.Customer object at 0x7feb9e39b810>
# >>> mod2.
# mod2.Location(    mod2.clean_data(
# >>> mod2.clean_data()
# cleaning data using mod2.clean_data()
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 08_python_packages % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import pkg
# >>> pkg
# <module 'pkg' (namespace)>

# >>> pkg.mod1.clean_data()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'pkg' has no attribute 'mod1'
# >>> pkg.mod2.Location()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'pkg' has no attribute 'mod2'
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 08_python_packages %
