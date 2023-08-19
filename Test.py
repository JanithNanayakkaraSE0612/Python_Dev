# def push(stack,value):
#     stack.append(value)

#     def pop(stack):
#         return stack.pop()
    
#     my_stack = []
#     push(my_stack, 'a')
#      push(my_stack, 'b')
#      push(my_stack, 'c')
#     my_stack['a','b','c']

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

my_stack = []
push(my_stack, 'a')
push(my_stack, 'b')
push(my_stack, 'c')
print(my_stack)  # Output should be: ['a', 'b', 'c']
