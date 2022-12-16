# list of dictionary
users = []
# Make a new user, and add them to the list.
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
    }
users.append(new_user)
# Make another new user, and add them as well.
new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
    }
users.append(new_user)
print(users)
for user in users:
    for k, v in user.items():
        print(k + ": " + v)
    print("\n")


# dictionary of list
# Store multiple languages for each person. 
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)

# dictionary of dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },  
    }

for username, user_dict in users.items():
    print("Username: " + username)
    full_name = user_dict['first'].capitalize() + " " + user_dict['last'].capitalize()
    location = user_dict['location'].capitalize()
    print("\tFullname: " + full_name)
    print("\tLocation: " + location)

# for username, user_dict in users.items():
#     print("\nUsername: " + username)
#     full_name = user_dict['first'] + " "
# full_name += user_dict['last']
# location = user_dict['location']
# print("\tFull name: " + full_name.title())
# print("\tLocation: " + location.title())