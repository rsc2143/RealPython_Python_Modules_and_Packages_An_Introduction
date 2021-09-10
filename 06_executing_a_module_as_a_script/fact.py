def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if(__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))

# Within this directory of 06_executing_a_module_as_a_script, if we launch a python3 session and type the following commands, we get the followin results

# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script % python
# Python 3.7.6 (default, Jan  8 2020, 13:42:34)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from fact import fact
# >>> fact(6)
# 720
# >>> exit()
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script % python fact.py 6
# 720
# (RealPython_Python_Modules_and_Packages_An_Introduction) (base) rohit@Rohits-MacBook-Air 06_executing_a_module_as_a_script %
