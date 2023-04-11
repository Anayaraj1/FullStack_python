#multiple inheritence

# class Animal:
#     name="Animals"

#     def __init__(self,animalname,animaltype):
#         self.animalname=animalname
#         self.animaltype=animaltype

#     def AnimalDetails(self):
#         print(f'Animal name is {self.animalname}\nAnimal type is {self.animaltype}')

num_rows = int(input("Please enter the number of rows"))
for i in range(num_rows,0,-1):
    for j in range(0, num_rows-i):
        print(end=" ")
    for j in range(0,i):
        print("* ", end=" ")
    print()