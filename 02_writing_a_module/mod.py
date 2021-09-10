s = 'Computers are useless. They can only give you answers'
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

# Within this directory of 02_writing_a_module, if we launch a python3 session and type the following commands, we get the followin results
# >>> import mod
# >>> mod.
# mod.Classy(  mod.a        mod.printy(  mod.s        
# >>> mod.a
# [100, 200, 300]
# >>> mod.printy()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: printy() missing 1 required positional argument: 'arg'
# >>> mod.printy('What is up')
# arg = What is up
# >>> x = Classy()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Classy' is not defined
# >>> x = mod.Classy()
# >>> x
# <mod.Classy object at 0x7fcf3db73fd0>
