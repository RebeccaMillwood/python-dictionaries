# Question 1

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }

# print(groceries)


# total = 0

# for item in groceries:
#     print(item)
#     quantity = input(f"How many {item} did you buy? ")
#     groceries[item] = groceries[item] * int(quantity)
#     total += groceries[item]
# print()
# print()
# a = ""
# print(f"====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item:<20} ${groceries[item]:.2f}")
# print(f"============================")
# print(f"{a:>20} ${total:.2f}")
# print()


# Question 2
# Given the list of names below, create a dictionary where each key is a name 
# and the value is the number of times that name occurs in the list.

# names = [
#     "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
#     "Joy", "Katie", "Maddie", "Tash", "Nic", 
#     "Rachael", "Bec", "Bec", "Tabitha", "Teagen", 
#     "Viv", "Anna", "Catherine", "Catherine", "Debby", 
#     "Gab", "Megan", "Michelle", "Nic", "Roxy", 
#     "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]
# print(names)

# names_dict = {}
# need to create this dictionary
# key = name
# value = number of times name appears in list

# for i in range(len(names)):
#     names_dict[names[i]] = 1
# # print(names_dict)

# for name in names_dict:
#     print(name, names_dict[name])


# for name in names:
# need to look in names list for 'name' then count/add to count when this name appears


# for name in names:
#     if name not in names_dict:
#         names_dict[name] = 1
#     else:
#         names_dict[name] = names_dict[name] +1  

# # print(names_dict)
# # for name in names_dict:
# #     print(name, names_dict[name])

# for key, value in names_dict.items():
#     print(key, value)

# print(names_dict)
# use this to test if dictionary works when above is programmed

# for key, value in names_dict.items():
#     print(key, value)

# print output of 'name' and 'number' of times appeared, e.g. Maddy 1
# won't work until there is data in the dictionary 


# Question 3

import csv

colours = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

print(colours)