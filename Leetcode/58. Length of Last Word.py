def step(s):
    s = "  fly to the moon "
    s = s.rstrip()
    count = 0
    for i in s[::-1]:
        if i != " ":
            count += 1
        else:
            break
    return count
