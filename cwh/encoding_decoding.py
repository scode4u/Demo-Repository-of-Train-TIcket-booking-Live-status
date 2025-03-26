# Program to enrypt and decrypt the messages in secret code language
import string
import random
res = ''.join(random.choices(string.ascii_letters,
                             k=7))
msg = input("Enter the message : ")
if len(msg) >= 3:
    encode = res+msg[1:]+msg[0:1]+res
    print("THe secret code is : "+encode)
else:
    print(msg[::-1])

print("Now decoding it's time to decode")

user = input("Enter D for decoding : ")
if (user == 'D' or user == 'd'):
    if len(encode) >= 3:
        print("The Original message is : "+encode[8:]+encode[-8]+encode[0:-8])
        
        