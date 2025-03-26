#  Public , private and protected
class Subject:

    def __init__(self):
        self.__name = "Suryansh Singh"
        self.name = "Suryansh Singh" # if don't use __ before variable name then it is public and can access via anywhere
         

info = Subject()
print(info.__name) # cannot access directly kyuki __ used to make private the variable
print(info._Subject__name) # can access directly by using _Class.Name__variable

