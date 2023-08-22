my_first_dict = dict()

#Using curly braces to initilialize a dictonary

scores = {'Saman':75,'Nimal':80,'Kamal':65}

print(scores['Saman'])
print(scores.get('Nimal'))

#Adding an element

scores ['Sunil'] = 60
print(scores)

#Updating an element

scores ['Saman'] =70
print(scores)

#Get the list of all keys

all_keys = list(scores.keys())
print(all_keys)

#Get the list of all values

all_values = list(scores.values())
print(all_values)