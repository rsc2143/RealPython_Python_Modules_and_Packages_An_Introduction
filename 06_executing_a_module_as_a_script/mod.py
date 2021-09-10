s = 'Computers are useless. They can only give you answers'
a = [100, 200, 300]

_should_not_be_imported_with_asterisk = 10

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

print('All of this not within __name__ == main control statement will be executed (in this case, printed) whether we execute mod.py using python mod.py or whether we import mod in the interpreter console')
print('Note that __name__ is equal to "main" if we execute using python mod.py')
print('Note that __name__ is equal to "mod" if we import mod in the intertpreter console')
print(s)
print(a)
printy('test')
x = Classy()
print(x)

if(__name__ == '__main__'):
    print('All of this within __name__ == main control statement will only be executed if we execute mod.py using python mod.py. It wont be executed if we import mod in the interpreter console')
    print('Note that __name__ is equal to "mod" if we execute using python mod.py')
    print('Note that __name__ is equal to "mod" if we import mod in the intertpreter console')

# Within this directory of 06_executing_a_module_as_a_script, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod
# All of this not within __name__ == main control statement will be executed (in this case, printed) whether we execute mod.py using python mod.py or whether we import mod in the interpreter console
# Note that __name__ is equal to "main" if we execute using python mod.py
# Note that __name__ is equal to "mod" if we import mod in the intertpreter console
# Computers are useless. They can only give you answers
# [100, 200, 300]
# arg = test
# <mod.Classy object at 0x7f9df739ee50>
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/Users/rohit/Downloads/Study/Python/RealPython_Python_Modules_and_Packages_An_Introduction/06_executing_a_module_as_a_script/mod.py", line 21, in <module>
#     sadas
# NameError: name 'sadas' is not defined
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script % python mod.py
# All of this not within __name__ == main control statement will be executed (in this case, printed) whether we execute mod.py using python mod.py or whether we import mod in the interpreter console
# Note that __name__ is equal to "main" if we execute using python mod.py
# Note that __name__ is equal to "mod" if we import mod in the intertpreter console
# Computers are useless. They can only give you answers
# [100, 200, 300]
# arg = test
# <__main__.Classy object at 0x7fd173a32d90>
# All of this within __name__ == main control statement will only be executed if we execute mod.py using python mod.py. It wont be executed if we import mod in the interpreter console
# Note that __name__ is equal to "mod" if we execute using python mod.py
# Note that __name__ is equal to "mod" if we import mod in the intertpreter console
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script %
