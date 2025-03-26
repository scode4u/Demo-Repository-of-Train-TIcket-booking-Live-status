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