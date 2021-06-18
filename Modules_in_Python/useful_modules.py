# Useful Modules in Python.

# apart from general data types, we are having specialized data types in python like below.

# collections.
# notice some of them are classes as they are with Capitals and other are functions.

# Counter can be used to count the number of items in the iterabale. This is very useful while
# doing the hash mapping.

from array import array
from datetime import date, time
from collections import Counter, defaultdict, OrderedDict
import datetime

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'Heyy you are a genius'

print(Counter(li))
print(Counter(sentence))

# default dict is used to do a default operation on a dictionary of the key is not found while accesing the dict.
# below is the example.

dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dict['c'])

# Ordered dict will memorize the order in which they are inserted into.

d1 = {'c': 100}
d1['a'] = 1
d1['b'] = 2

d2 = {'c': 100}
d1['a'] = 1
d1['b'] = 2

# When we comapre dict it is going the check the values in the positions.
print(d1 == d2)
# The above resut is false as it is not an ordered dict. Below example is to create an ordered dict.

d3 = OrderedDict({'c': 100})
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict({'c': 100})
d4['a'] = 1
d4['b'] = 2
print(d3 == d4)


# Tidbit
# older versions of python3.7 need to use ordered dictionaries. As in the latest versions
# of Python regular dictionaries are even ordered so no need of using the ordered dicts.


# some other useful  modules in python datetime()


print(time(5, 45, 2))
# We can create the time objects here.

# Below gives the today's date.
print(date.today())

# There are alot functions we can do on the datetime.

# Another useful package is array.
# Lists in python are arrays.
# Arrays in python rake up less memory and imporves perforamnce in python.


arr = array('i', [1, 2, 3])

print(arr[0])
