# Passing info to function.
def describe_pet(animal, name):
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Using keyword arguments
describe_pet(animal='hamster', name='harry')
describe_pet(name='willie', animal='dog')

# Using a default value
def describe_pet1(name, animal='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")

describe_pet1('harry', 'hamster')
describe_pet1('willie')

# Using None to make an argument optional
def describe_pet2(animal, name=None):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    if name:
        print("Its name is " + name + ".")

describe_pet2('hamster', 'harry')
describe_pet2('snake')       

# Returning a dictionary with optional values
def build_person(first, last, age=None):
    """Return a dictionary of information
    about a person.
    """
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', 27)
print(musician)
musician = build_person('janis', 'joplin')
print(musician)