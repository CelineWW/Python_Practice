# Using a loop to generate a list of square numbers
squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)

print(squares)

# Using a comprehension to generate a list of square numbers
powers = [x**3 for x in range(1, 11)]
print(powers)


# Using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

# Using a comprehension to convert a list of names to upper case
lower_names = [name.lower() for name in names]
print(lower_names)

capital_names = [name.capitalize() for name in names]
print(capital_names)