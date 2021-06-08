#Lists
# These are denoted with [] brackets. Lists are form of the arrays.

li = [1,2,3,4,5,6]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

#Data Structure - This is the first type of the data structure.
#amazon_cart = ['notebooks','sunglasses']
#print(amazon_cart[0])

#Lists Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

#[start:stop:step]

#print(amazon_cart[::1])

#Lists are Mutable
# Copying list is different from modifying the list.
# lists should be copied like new_list = old_list[:]
amazon_cart[0] = 'laptops'
new_cart = amazon_cart[:]
new_cart[0] = 'Deo'
print(amazon_cart)
print(new_cart)


#List Methods
basket = [1,2,3,4,5]

#adding - Appending/Insert - This will not output new list, it only updates the list
basket.append(100)  #This will not produce any output as the result.
new_list = basket
basket.insert(4,10)
basket.extend([400,500])
print(basket)
#print(new_list)

#Removing methods
basket.pop()   #Here index is given
basket.remove(4)   #Here value is given
print(basket)

basket.clear()

print(basket)

#Important understanding is pop returns the item which is being removed.

#Lists Methods 2
basket = ['a','b','c','d','e']
print(basket.index('e',0,5))
print(basket.count('d'))


#Lists Methods 3 - Sorting using list methods .sort()
basket = ['x','b','c','d','e']
new_basket = basket.copy()
print(sorted(basket))
basket.sort()
print(basket)
new_basket.sort()
print(new_basket)

#Reversing the lists.
basket = [1,5,4,3,6,7,8,9,0]
print(basket)
basket.sort()
basket.reverse()
print(basket)


######Common List Patterns.
print(len(basket))
print(basket[:])
print(basket[::-1])

print(list(range(0,101)))

new_sentence = '.'.join(['100','120','130'])
print(new_sentence)

#List Unpacking
a,b,c,*other,d = [0,1,2,3,4,5,6,7,8,9]
print(a,'\n',b,'\n',c,'\n',other,'\n',d)
print(type(a))
print(type(other))