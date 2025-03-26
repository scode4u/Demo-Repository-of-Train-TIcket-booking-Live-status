
def r(haystack, needle):   
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
print(r("sadbutsad" ,"sad"))