import itertools

def get_city(person):
    return person['city']

people = [
    {
        'name': 'John',
        'city': 'Berlin'
    },
    {
        'name': 'Mary',
        'city': 'Berlin'
    },
    {
        'name': 'Bob',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi',
        'city': 'Tallinn'
    },
    {
        'name': 'Marika',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul',
        'city': 'Dubai'
    },
    {
        'name': 'Mary',
        'city': 'Dubai'
    },
    {
        'name': 'Marika',
        'city': 'Tallinn'
    },
    {
        'name': 'Bob',
        'city': 'Berlin'
    }
]
people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, key=lambda x: x['city'])
copy1, copy2 = itertools.tee(result)
for key, group in copy1:
    print(key)
    for item in group:
        print(item)


def sort_second(x):
    return x[1]
sample = [[1, 4], [5, 3], [2, 10], [6, 1]]
sample.sort(key=lambda x: x[1])
print(sample)

def last_letter(name):
    return name[-1]
names = ['Jack', 'Sarah', 'Mary', 'Johhny']
# names.sort(key=last_letter)
print(sorted(names, key=lambda x: x[-1]))
print(names)

a = lambda x, y: x ** y
print(a(5, 10))
a = lambda x, y, r: x * y + r
