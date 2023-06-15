# Remove element from list
# a = [1, 2, 3, 10, 24, 35, 67]
# b = [8, 9, 2]

# print(b+a)
# print(len(a))

# pop function
# popes_item = a.pop(1)
# print(popes_item)
# print(a)

# popes_item = a.pop(-3)
# print(popes_item)
# print(a)

# popes_item = a.pop() if no indexing position is given then it remove from last
# print(popes_item)
# print(a)

# Remove an item by value: remove()
# a = [1, 2, 3, 10, 24, 35, 67]
# b = [8, 9, 2]

# a.remove(10)  # in remove we cannot use indexing position we have to write element
# print(a)

# del()
# l = [0, 10, 20, 35, 67, 43, 24]
# del l[1]
# print(l)

# del l[2:5]
# print(l)
# output:-    #[0, 10, 43, 24]

# del l[:]
# print(l)
# output:- #[]

# List comprehensions in Python
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = [i for i in l if i % 2 == 0]
# print(even)

# odd = [i for i in l if i % 2 != 0]
# print(odd)

# print(l)

# Add element in a list

# append()
# insert()
# extend()
# +

# append()
# fruit_list = ["Apple", "Banana"]
# print(f'current list in fruit:- \n{fruit_list}')

# new_fruit = input("Enter the fruit which you want to add:-\n")
# fruit_list.append(new_fruit)

# print(f'updated fruit list\n{fruit_list}')
# print(fruit_list)

# insert()
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# num_list = [1, 2, 3, 4, 5]

# print(f'current list{num_list}')

# num = int(input("Please enter the num you want to add"))

# index = int(input(f'Please enter the index between 0 and {len(num_list)-1} to add the number:\n'))

# num_list.insert(index, num)
# print(f'updated num list{num_list}')
# print(len(num_list))

# extend()
# extent_list = []
# extent_list.extend([1, 3])
# print(extent_list)

# extent_list.extend([10, 29])
# print(extent_list)

# extent_list.extend("ABC")
# print(extent_list)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
