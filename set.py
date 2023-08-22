# creating sets in python 

#using curly braces


fruits = {'apple','orange','banana'}
print(fruits)

#Using set constructor

fruits = set (['apple','orange','banana'])
for item in fruits:
    print(item)
#print(fruits)
#print(len(fruits))

#add single element
fruits.add('mango')
print(fruits)

#add multiple element
fruits.update(['Red','Blue'])
print(fruits)

fruits.remove('Red')
fruits.discard('mango')
print(fruits)
fruits.pop()
print(fruits)

A = {1,2,3,4,5}
B = {1,3,5,7,9}
print(A|B)

#Using Union method

print(A.union(B))

#set Differnce

print(A-B)

#Using differnce () method

print(A.difference(B))