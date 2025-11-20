#Jc 
# List of places I would like to visit)
places = ["Japan", "France", "Dubai", "Italy", "Egypt"]

# Original order
print("Original list:")
print(places)

# Alphabetical order 
print("\nList in Alphabetical Order:")
print(sorted(places))

# Confirming original list is unchanged
print("\nOriginal list again:")
print(places)

# Reversing alphabetical order 
print("\nReverse alphabetical order :")
print(sorted(places, reverse=True))

# Confirming original list is still unchanged
print("\nOriginal list again:")
print(places)

# Reversing order of the list 
places.reverse()
print("\nList after using reverse():")
print(places)

# Reversing again to get original
places.reverse()
print("\nList after reversing again:")
print(places)

# Using sort() to change the list to alphabetical order
places.sort()
print("\nList after using sort() (alphabetical):")
print(places)

# Using sort() again to change the list to reverse alphabetical order
places.sort(reverse=True)
print("\nList after using sort(reverse=True) (reverse alphabetical):")
print(places)
#Jc