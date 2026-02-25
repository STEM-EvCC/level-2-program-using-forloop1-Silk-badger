#Basic for Loop
#A for loop is used for iterating over a set of range of values
grocery_list = ["eggs", "milk", "pizza", "cereal"]
#for each item x, print the item.
for x in grocery_list:
    print(x)


#Printing each letter in a word
for x in "Snorlax":
    print(x)

# We can use break to stop the loop before it loops through all items
for x in grocery_list:
    if x == "pizza":
        break
    print(x)

print("")
print("")

#we can use continue to stop the current iteration of the loop and continue to the next
for x in grocery_list:
    if x == "pizza":
        continue
print(x)

#we can use range() to iterate a specific number of times
# note that range uses index values
for x in range(8):
    print(x)

# we can use else keword in conjunction with for loop to execute code when the loop is finished
for x in range(4):
    print(x)
else:  
    print("Sequence finished")

#Nested For Loops
spooky_adjectives = ["Frightful", "Scary", "Haunting"]
monster_list = ["Ghost", "Mummy", "Mike Wazowski"]

for x in spooky_adjectives:
    for y in monster_list:
        print(x,y)

#For loops CANNOT be empty

#This is wrong
mission_counter = []
