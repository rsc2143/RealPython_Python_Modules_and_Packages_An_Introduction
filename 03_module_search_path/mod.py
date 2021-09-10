s = 'Computers are useless. They can only give you answers'
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

# Within this directory of 03_module_search_path, if we launch a python3 session and type the following commands, we get the followin results
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 02_writing_a_module % python3
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> sys.path
# ['', '/Library/TeX/texbin/xelatex', '/Users/rohit/opt/anaconda3/lib/python37.zip', '/Users/rohit/opt/anaconda3/lib/python3.7', '/Users/rohit/opt/anaconda3/lib/python3.7/lib-dynload', '/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/lib/python3.7/site-packages']
# >>> import mod
# >>> mod.__file__
# '/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/02_writing_a_module/mod.py'
# >>> re.__file__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 're' is not defined
# >>> import re
# >>> re.__file__
# '/Users/rohit/opt/anaconda3/lib/python3.7/re.py'
# >>> sys.path.append(r'/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/02_writing_a_module/')
# >>> sys.path
# ['', '/Library/TeX/texbin/xelatex', '/Users/rohit/opt/anaconda3/lib/python37.zip', '/Users/rohit/opt/anaconda3/lib/python3.7', '/Users/rohit/opt/anaconda3/lib/python3.7/lib-dynload', '/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/lib/python3.7/site-packages', '/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/02_writing_a_module/']
