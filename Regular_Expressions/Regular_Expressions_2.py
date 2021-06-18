# Regular Expressions

# Regular Expressions itself is a kind of language.
# https://regex101.com/  - This is a super cool website to experiment on Regular expressions.

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

a = 'gliv@hh.com'

print(pattern.search(a))
