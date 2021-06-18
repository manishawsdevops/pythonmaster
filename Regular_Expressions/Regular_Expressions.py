# Regular Expressions.

# Regular Expressions itself is a kind of language.
# https://regex101.com/  - This is a super cool website to experiment on Regular expressions.

# https://regexone.com/ - This is where you can learn more about regex.
# They are not python specific. We can use it anywhere.
# Regular expressions after searching not just prints true or false but it gives the match object.

import re

string1 = 'Searching the regular expressions'
a = re.search('Searc', string1)
print(a.start())
print(a.end())
print(a.group())

# We can also craete patters in regular expressions
# To create the regular expression packages the syntax is <pattern_var> = re.compile('<pattern>')

pattern1 = re.compile('regular')

print(pattern1.match(string1))
print(pattern1.search(string1))
print(pattern1.findall(string1))
print(pattern1.fullmatch(string1))
