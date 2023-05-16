fruits = ["apple", "banana", "orange"]
def mylist():
#Create 
    fruits.append("grape")  # Adds "grape" to the end of the list
    fruits.insert(1, "mango")  # Adds "mango" at index 1, shifting other items

# Read (Accessing items)
    print(fruits[0])  # Output: "apple"
    print(fruits[2])  # Output: "orange"

    print(fruits[-1])  # Output: "orange"
    print(fruits[-2])  # Output: "banana"

#Update (Modifying items)
    fruits[1] = "pineapple"  # Modifies the item at index 1 to "pineapple"

#Delete (Removing items)
    fruits.remove("apple")  # Removes the item "apple" from the list
    del fruits[0]  # Removes the item at index 0 from the list

    removed_item = fruits.pop(1)  # Removes the item at index 1 and returns it
    print(removed_item)  # Output: "banana"

mylist()