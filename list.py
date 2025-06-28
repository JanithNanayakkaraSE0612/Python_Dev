x = [12,434,56,23,45,67,89,90,100]
y=[0,1,2,3,4,5,6,7,8,9]
z=x+y # special operator in list can only just to add two lists together
print(z)
print(9 in z)  # Check if 9 is in the list z
a = 10 not in z  # Check if 10 is not in the list z
print(a)  # Print the result of the check
print(x)  # Print the list
print(type(x))  # Print the type of the list
print(x[0])  # Access the first element of the list     
x[0] = 1000  # Change the first element of the list
print(x)  # Print the modified list
x.append(200)  # Append a new element to the list
print(x)  # Print the list after appending
x.insert(1, 500)  # Insert a new element at index 1
print(x)  # Print the list after inserting
x.remove(56)  # Remove the element 1000 from the list
print(x)  # Print the list after removing
x.pop(2)  # Remove the element at index 2
print(x)  # Print the list after popping
