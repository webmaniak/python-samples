print("------------------------------")
print("Ordered dictionaries")
print("------------------------------")

from collections import OrderedDict

# The favorite_languages dictionary will preserve the order of insertion
# unlike a standard dictionary.
favorite_languages = OrderedDict()
favorite_languages['bob'] = 'python'
favorite_languages['jean'] = 'java'
favorite_languages['sarah'] = 'php'
favorite_languages['mary'] = 'c#'

for name, language in favorite_languages.items():
    # Reminder: .title() does an upercase of the first character
    print(name.title() + '\'s favorite language is ' + language.title())