#1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
'''
a=[x for x in range(1200,2000,130)]
print(a)
'''
#2. Use list comprehension to construct a new list but add 6 to each item.
'''
l=[1,2,3,4,5,6,7]
add=[6+i for i in l]
print(add)
'''
#3.Using list comprehension,construct a list from the squares of each element in the list.
'''
ls=[2,3,8,12,14]
sqr=[2**x for x in ls]
print(sqr)
'''
#4.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
'''
ls=[2,3,6,7,8,10,11]
sqr=[i**2 for i in ls if i>7]
print(sqr)
'''
#5.Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
print([i.upper() for i in dict])
