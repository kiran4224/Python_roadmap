### https://docs.python.org/3/library/functions.html

#A
abs() # Returns a absolute value of a number. The argument may be intger, float or object implementing __abs__() , if complex number passed it magnitude is returned

aiter() # Returns a asynchronous iterator for an asynchronous iterable 
all() # Return True if all elements of the iterable are true
anext() #  awaitable anext(async_iterator), returns next item from the given asynchronous iterator
any() #  returns true if any element of the iterable is True , Returns flase if iterable is empty
ascii() # returns stirng represented object while adding escape characters to non ASCII characters: repr() gives the same out for non ascii characters
"""
>>> ob = "sijaoviamoi1é, à, ö, ñ, etc."
>>> ascii(ob)
"'sijaoviamoi1\\xe9, \\xe0, \\xf6, \\xf1, etc.'"
>>> repr(ob)
"'sijaoviamoi1é, à, ö, ñ, etc.'"
"""

# B
bin()            # convert integer to binary string
bool()           # check true or false and returns the same
breakpoint()     # System 
  """
  This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. 
  By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t 
  have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and 
  breakpoint() will automatically call that, allowing you to drop into the debugger of choice. If sys.breakpointhook() is not accessible, this 
  function will raise RuntimeError.
  By default, the behavior of breakpoint() can be changed with the PYTHONBREAKPOINT environment variable. See sys.breakpointhook() for usage details.
  Note that this is not guaranteed if sys.breakpointhook() has been replaced.
  Raises an auditing event builtins.breakpoint with argument breakpointhook.
"""
bytearray()
"""
class bytearray(source=b'')
class bytearray(source, encoding)
class bytearray(source, encoding, errors)
"""

bytes()
'''
    class bytes(source=b'')
    class bytes(source, encoding)
    class bytes(source, encoding, errors)
    
'''
# C
callable()      # Return True if the object argument appears callable, False if not. 
chr()           # Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().
classmethod()
compile()
"""
 compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
 Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). 
 source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.
 The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).
 The mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence of statements, 'eval' if it consists of a single expression, 
 or 'single' if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than None will be printed).
"""

complex()

D
delattr()
dict()
dir() # Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
divmod()

	
E
enumerate()
eval() #**************************************
exec() #**************************************
"""
This function supports dynamic execution of Python code. object must be either a string or a code object.
If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs)
"""

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
	
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()




	
R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

