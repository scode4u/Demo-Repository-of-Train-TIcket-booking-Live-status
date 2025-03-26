# Seek()
with open('file.txt','r') as f:
    print(type(f))
    f.seek(10) # by using the seek funtion , it will read character after 10 byte 

    data = f.read(5) # it will read the data after 10 digits 
    print(data)
    #  if you wanna know , till which digit seek function is used
    print(f.tell())
    