nums = [1,9]
s = int(''.join([str(i) for i in nums]))
s += 1
result = list(str(s))
print([int(i) for i in result])