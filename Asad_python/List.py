# name = "Asad"
# age = 10
# country = "UAE"
# habby = "Coding"

# Asad = ["Asad",10,"UAE","Coding"]

# Main concepts: what is list, indexing, append(), remove()



# Indexing

backpack = ['compass','icepick','walkieTakie','food','water',1,1,1,16,66]
print(backpack)

print(backpack[3])
print(backpack[4])


print(backpack[-4])


print(backpack[0]) # to pick the first item
print(backpack[-1]) # to pick the last item



# how to add the data
# append() - it always add the new data in the end of your list

backpack.append("Monty")
print(backpack)
print(backpack[-1])



# how to remove the data
# pop() - it will alwys remove the last data
backpack.pop()
print(backpack)

# remove() - mention the data you want to remove

backpack.remove('food')
print(backpack)
