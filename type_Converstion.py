a = "10"
b = 20
# cannot run  this line cannot  multple value because int and string diff data types
# c = a+b
c=int(a) + b  # Convert string to int before addition
# Now c will be an integer
print(c)    

j="false"
k=10

m = bool(j) +k
print(m)# Convert string to boolean


o = input()
p=20

l = int(o) + p  # Convert input string to int before addition
print(l)  # Now l will be an integer

print("Enter your name:",end=' ') # end=' ' using same line operate
name = input()  # Input will be a string        
print("Hello, " + name + "!")  # Concatenate string with input name