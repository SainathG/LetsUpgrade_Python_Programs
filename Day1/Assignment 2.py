lst1 = ["a", "b", "c","e","d","f","h","g"]
lst2 =["p","q","s","r","t"]
print(lst1[1])
print(lst1[:4])            # Print the information from start to given position index

print(lst1.pop(2))         # Removes element based on the index position
print(lst1)

lst1.remove("d")           # Removes the specified element
print(lst1)

lst1.extend(lst2)          # To append elements from another list to the current list.
print(lst1)

lst1.sort()                # sort the list ascending, by default
print(lst1)

lst1.sort(reverse=True)    # sort the list descending
print(lst1)

lst2.reverse()             # Reverses the order of the list
print(lst2)


