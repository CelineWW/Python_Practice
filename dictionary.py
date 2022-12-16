# Looping through all key-value pairs
# Store people's favorite languages.
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in fav_languages.items():
    print(name + ": " + language)

# Looping through all the keys   
for name in fav_languages.keys():
    print(name)

# Looping through all the values
for language in fav_languages.values():
    print(language)

# Looping through all the keys in order
# Show each person's favorite language, in order by the person's name.
for name, language in sorted(fav_languages.items()):
    print(name + ": " + language)