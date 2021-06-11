#Highest even in the list.


def highest_even(li):
    li.sort(reverse=True)
    for i in li:
        if i % 2 == 0:
            return i

print(highest_even([2,10,2,3,4,8,11,28]))