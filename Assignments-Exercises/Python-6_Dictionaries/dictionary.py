libro = {'name': 'Mouse', 'age': 18}
print("\nOriginal dictionary:", libro)

# add a new key-value pair to the libro
libro['city'] = 'Topia'
print("Added key-value:", libro)

# update an exsisting key-value pair 
libro['name'] = 'Akla'
print("Update value of name:", libro)

# delete age key-value
del libro['age']
print("Removed age:", libro)

print("\n")

# add new key-value pair
libro['hobby'] = 'gaming'
print("Added hobby key-value:", libro)

# pop
val = libro.pop('city')
print("Removed city:", libro)
print("Popped value:", val)