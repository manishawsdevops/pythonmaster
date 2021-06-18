# Password Validation Exercise
# https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/

# At least 8 characters long
# Can contain any sort of characters like !@#$$
# ^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$
# "^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%&]).{8,32}$"

# ^                                            Match the beginning of the string
# (?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
# (?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
# (?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
# (?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\])    Require that at least one special character appear anywhere in the string
# .{8,32}                                      The password must be at least 8 characters long, but no more than 32
# $                                            Match the end of the string.


import re

pattern = re.compile(
    r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%&]).{8,}$")

password = 'LionHoney@1994'

print(pattern.fullmatch(password))
