# Allowing a function to modify a list
def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print("\nUnprinted:", unprinted)
print("Printed:", printed)

# Preventing a function from modifying a list
original = ['phone case', 'pendant', 'ring']
printed = []
print_models(original[:], printed)
print("\nOriginal:", original)
print("Printed:", printed)


