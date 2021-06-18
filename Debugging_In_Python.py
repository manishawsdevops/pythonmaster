# Debugging in Python.
# Act of finding errors and fixing errors are called Debugging.

# Recommendations for Debuging.
'''
    1. Use Linting - Like that pyflakes using in the visual code.
        These allows us to find the errors even when run those.
    2. IDE - Start using IDE/Editors. As all these have the autoformatting,
        and allows us to detect the errors by highlighting.
    3. Read Errors - We should be able to read errors while coding in the python.
        Read and understand the errors in python.
    4. PDB - Python Debugger - It is built module in python.
        We can read about in the documentaiton. Use it as <import pdb>
        step - we can use this command to go to next line.
        continue - will continue the program
        a - Will give all the arguments of the current function.
        w - shows the context of the current line which is executing.
        Once you are done with the debugging you can remove it.
        We are also able to change the values while using debugging.
'''

import pdb


def summ(n1, n2):
    pdb.set_trace()
    t = 5*3
    return n1+n2


print(summ(1, 'dkfbnoifd'))
