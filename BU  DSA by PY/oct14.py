# # stack = []
# # min_stack = []

# # n = int(input("Enter the number of elements: "))
# # for i in range(n):
# #     item = int(input("Enter element: "))
# #     stack.append(item)
# #     if not min_stack or item <= min_stack[-1]:
# #         min_stack.append(item)

# # print("Minimum element:", min_stack[-1])



# # def push(stack, top, min_item, item):
# #     stack.append(item)
# #     top += 1
# #     if item < min_item:
# #         min_item = item
# #     return top, min_item

# # stack = []
# # top = -1
# # min_item = float('inf')

# # n = int(input("Enter the number of elements: "))
# # for i in range(n):
# #     item = int(input("Enter element: "))
# #     top, min_item = push(stack, top, min_item, item)

# # print("Minimum element:", min_item)


# n = int(input("Enter the number\t:"))
# top = -1
# for i in range(n):
#     item = int(input("Enter the item\t:"))
#     stack, top = push(stack, top, 10, item)
      
# print(stack,top)


#  another 

def push(stack,top,Max,item):
    if top==Max-1:
        print("Overflow")
    elif stack[top] == -1:
        top += 1
        stack[top] = item
    else:
        if item < stack[top]:
            top=top+1
            stack[top]=item
        
    return (stack,top)

def pop(stack,top):
    if top==-1:
        print("Underflow")
    else:
        temp = stack[top]
        stack[top] = -1
        top = top - 1
    return (stack,temp)

stack = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

n = int(input("Enter the number\t:"))
top = -1
for i in range(n):
    item = int(input("Enter the item\t:"))
    stack, top = push(stack, top, 10, item)
      
print(stack,top)

# another
n = int(input("Enter the number of elements: "))

stack = [-1] * n
top = -1
min_item = float('inf')

for i in range(n):
    item = int(input("Enter element: "))
    
    if item < min_item:  # Only insert if the new item is smaller
        top += 1
        stack[top] = item  # Replace -1 with the new item
        min_item = item

print("Stack:", stack)
print("Minimum element:", min_item)
