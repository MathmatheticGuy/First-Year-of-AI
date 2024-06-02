names: list[str] = ['Jame', 'Harvestedor', 'Martin', 'Josepf Stalin']

#? Instead of this 
# long_name: list[str] = [] #? list with annotation. This is no diff than long_name = []
# for people_name in names:
#     if len(people_name) > 7:
#         long_name.append(people_name)


#? Use List Comprehension like this (more performance but might decrease readbility)
long_name: list[str] = [
    name for name in names 
    if len(name) > 9
]

results = [
    x if x % 2 == 0 
    else -x 
    for x in range(10)
]

print(f'x: {results}')
print(f'long name {long_name}')

