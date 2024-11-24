# a=['hell','world','how','are','you']
# for i in a:
#     print(i,end='  ')

# # #------------------------------------------------------------------------------
# print('What is your name?')   # ask for their name
# # my_name = input()
# # print('Hi, {}'.format(my_name))
# # #------------------------------------------------------------------------------
# str='hello'
# list1=list(str)
# print(list1)
# print(list1.count('l'))
# l=list(reversed(list1))
# print(l)
# print(''.join(l))
# # #--------------------------------------------------------------------------------
# my_string = "Hello, World!"
# reversed_string = my_string[::-1]
# print(reversed_string)
# # #--------------------------------------------------------------------------------
# age = 15

# # this ternary operator:
# print('kid' if age < 13 else 'teen' if age < 18 else 'adult')

# # is equivalent to this if statement:
# if age < 18:
# 	if age < 13:
# 		print('kid')
# 	else:
# 		print('teen')
# else:
# 	print('adult')
# # #--------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)  # Output: [1, 4, 9, 16]
# # #--------------------------------------------------------------------------------
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8
# # #--------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6]
# # #--------------------------------------------------------------------------------
# def power(n):
#     return lambda x: x ** n

# square = power(2)
# cube = power(3)

# print(square(4))  # Output: 16
# print(cube(2))    # Output: 8

# # #-------------------------------------------------------------------------------
# nested_lambda = lambda x: lambda y: x + y
# add_five = nested_lambda(5)
# print(add_five(10))  # Output: 15
# # #-------------------------------------------------------------------------------
# words = ['banana', 'apple', 'grape', 'orange']
# sorted_words = sorted(words, key=lambda word: len(word))
# print(sorted_words)  # Output: ['apple', 'grape', 'banana', 'orange']
# # #-------------------------------------------------------------------------------
# words = ['a', 'list', 'of', 'words']
# lengths = list(map(lambda word: len(word), words))
# print(lengths)  # Output: [1, 4, 2, 5]
# # #-------------------------------------------------------------------------------
# furniture = ['table', 'chair', 'rack', 'shelf']
 
# price = [100, 50, 80, 40]

# for item, amount in zip(furniture, price):
#     print(f'The {item} costs ${amount}')
# # The table costs $100
# # The chair costs $50
# # The rack costs $80
# # The shelf costs $40
# # #-------------------------------------------------------------------------------
# names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

# new_list = []
# for n in names:
#     if n.startswith('C'):
#         new_list.append(n)
# print(new_list)
# # ['Charles', 'Carol']
# # #-------------------------------------------------------------------------------
# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam.strip('ampS'))  # Output: BaconSpamEggs
# # #-------------------------------------------------------------------------------
# fruits = "apple, banana, cherry, apple"
# print(fruits.replace("apple", "orange", 1)) # Output: orange, banana, cherry, apple
# # #-------------------------------------------------------------------------------
# with open('file.txt','a') as file:
#     file.write(' \nhello world')
# # #-------------------------------------------------------------------------------
# with open('file.txt','r') as file:
#     content=file.readlines()
#     for item in content:
#         # print(item,end='')
#         print(item.strip())
# print(content)
# # #-------------------------------------------------------------------------------
# import os

# if os.path.exists("file.txt"):
#     with open("file.txt", "r") as file:
#         print(file.read())
# else:
#     print("File does not exist.")
# # #--------------------------------------------------------------------------------
# list(filter(lambda x : x % 2 == 1, range(1, 20)))
# # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# [x ** 2 for x in range (1, 11) if  x % 2 == 1]
# # [1, 9, 25, 49, 81]

# [x for x in [3, 4, 5, 6, 7] if x > 5]
# # [6, 7]

# list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
# # [6, 7]
# # #--------------------------------------------------------------------------------

# st = "hello faraz how are you"
# strt = st.split(' ')
# for w in strt:
#     data=reversed(w)
#     print(''.join(data),end=' ')
# #--------------------------------------------------------------------------------