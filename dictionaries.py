pet = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud'
}

pet['age_years'] = 2

print(pet)
print(pet.values())
print(pet.keys())


set1 = {1, 2, 3, 4, 5}
set2 = set([4, 5, 6, 7, 8])
print({"set1": type(set1), "set2": type(set2)})
print(set1.union(set2))