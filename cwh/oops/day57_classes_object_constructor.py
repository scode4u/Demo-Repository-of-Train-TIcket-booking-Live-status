class Solution:

    def __init__(self, n, o):
        self.name = n
        self.occuptaion = o

    def information(self):
        print(f"{self.name} is a experinced {self.occuptaion}")

obj = Solution("Suryansh Singh" , "Data Scientist")
obj.information()


