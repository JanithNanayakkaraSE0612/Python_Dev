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