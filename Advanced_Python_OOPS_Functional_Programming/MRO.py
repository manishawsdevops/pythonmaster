# Method Resolution Order
# Depth First Search

# MRO Algorith
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass
