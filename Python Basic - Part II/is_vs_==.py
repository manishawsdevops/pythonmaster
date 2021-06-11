# there are cases where we get confused with 'is' and ==
# == this checks for the equality of the value.
# is this checks for the exact same value in the same memory address location.


print(True == False)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is False)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
a = [1,2,3]
b = [1,2,3]
print(a is b)
