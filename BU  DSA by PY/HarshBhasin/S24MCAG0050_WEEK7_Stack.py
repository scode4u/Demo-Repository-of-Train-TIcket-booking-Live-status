def push(stack, top, max_size, item):
    if top == max_size - 1:
        print("Overflow")
    else:
        top += 1
        stack[top] = item
    return stack, top

def pop(stack, top):
    if top == -1:
        print("Underflow")
    else:
        temp = stack[top]
        top -= 1
        print(temp)
    return stack, top

max_size = 5
stack = [-1] * max_size
top = -1

print(stack, top, max_size)

stack, top = push(stack, top, max_size, 10)
print(stack, top, max_size)

stack, top = push(stack, top, max_size, 13)
print(stack, top, max_size)

stack, top = push(stack, top, max_size, 11)
print(stack, top, max_size)

stack, top = push(stack, top, max_size, 4)
print(stack, top, max_size)

stack, top = push(stack, top, max_size, 7)
print(stack, top, max_size)

stack, top = pop(stack, top)
print(stack, top, max_size)

stack, top = pop(stack, top)
print(stack, top, max_size)

stack, top = pop(stack, top)
print(stack, top, max_size)

stack, top = pop(stack, top)
print(stack, top, max_size)

stack, top = pop(stack, top)
print(stack, top, max_size)
