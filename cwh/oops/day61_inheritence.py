class Employee:

    def __init__(self, name , id):
        self.name = name
        self.id = id

    def information(self):
        print(f"The id of {self.name} is {self.id}")

info = Employee("Suryansh Singh" , "S24MCAG0050")
info.information()