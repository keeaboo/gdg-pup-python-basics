# first list
listahan = [3, 14, 20, 25, 19]
print("Original list: ", listahan)

listahan.append(0)
print("List after adding an element: ", listahan)

listahan.remove(19)
print("List after removing an element: ", listahan)

listahan.sort()
print("List after sorting: ", listahan)

# second list
listwo = [10, 8, 7, 5, 3]
print("\nAnother list: ", listwo)

# stores the sorted listwo to another list without changing it directly
list = sorted(listwo)

# prints the sorted list
print("Sorted list using sorted():", list)