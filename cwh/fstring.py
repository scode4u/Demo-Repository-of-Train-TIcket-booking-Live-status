string = "My name is {} and i am from {}"
name = "Suryansh Singh"
country = "India"

# Old method
print(string.format(name, country)) # format is a function that is used to print the name and country 

# New method
print(f"My Name is {name} and i am from {country}") # convinient

