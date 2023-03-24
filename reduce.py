from functools import reduce
from itertools import accumulate

person = {'name': 'George', 'birth_year': 1943, 'city': 'Liverpool'}
description = {'name': 'George Harrison', 'band': 'The Beatles', 'alive': False}
additional = {'career': '1957-2001', 'religion': 'Hindu'}
family = {'spouses': ['Pattie Boyd', 'Olivia Arias'], 'children': 'Dhani'}

# person.update(description)
# print(person)
# # person.update(description)
# # print(person)
# person.update(additional)
# print(person)
# person.update(family)
# print(person)

# The solution based on https://stackoverflow.com/a/15714097/1899061:

print(reduce(lambda x, y: x.update(y) or x, [person, description, additional, family], {}))
# print(reduce(lambda x, y: x.update(y), [person], {}))
# print(reduce(lambda x, y: x.update(y) or x, [], {}))
# print(reduce(lambda x, y: x.update(y), [], {}))

# Note that it must be x.update(y) or x, not just x.update(y).
# The reason is that dict.update() always returns None.
# If there is only one dict in the list, the result of x.update(y) is None (run the first commented line from above).
# If there are more than one dicts in the list, the next x.update(y) will essentially try None.update(y) (error).
# The initializer {} handles the empty list situations (the second and the third commented lines above).

# The solution based on https://stackoverflow.com/a/60195034/1899061 (but only 'repeats the entire reduce' 4 times):

print()
print(list(accumulate([person, description, additional, family], lambda x, y: x.update(y) or x))[0])
