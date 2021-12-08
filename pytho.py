# #! DATA TYPES

# #! str -> string
# #! int -> integer
# #! bool -> True(1), False(0)
# #! dict -> dictionary
# #! list -> 
# #! set ->
# #! tuple ->


# #? STRING
string1 = 'a'
string2 = "a"
string3 = """a
a
a
a""" # створення довгих рядків
string4 = '''a
a
a
''' # створення довгих рядків

string = 'string'
# string = string.capitalize() #? Верхній реєстр першої букви
# string = string.casefold() #? Переводе в нижній реєстр
# string = string.upper() #? transfer all into uppercase
# string = string.lower() #? transfer all into lowercase
# string = string.count('letter from the string') #? count all the same letters
# string = string.startswith("st") #? we will get boolean True if the this letter is the first letter of the string else False
# string = string.endswith("ing") #? we will get boolean True if the this letter is the last letter of the string else False
# string = string.index('r') #? display index of the letter
# string = string.find('r') #? display index of the letter
# string = string.replace('st','St') #? raplase letters (from old?, to new)
# string = string.title() #? transfer first letter to uppercase
# string = string.swapcase() #? swapcase of all letters
# string = string.split('s') #? split the string by the letter(s)
# string = string.strip() #? remove all spaces from the edge of the word(s)
# string = string.zfill(10) #!
# string = string.join() #* 


# print(string)
# #! INTEGERS
# integer1 = 1
# decimal2 = Decimal() десяток
# fraction = Fraction() дробь
# 2j + 1
# a = 3
# b = 2
# c = 0
# c = a // b
# c = 3 % 2
# c **= a


# print(c)


# #! BOOLEAN

# print(3 > 3)


# #! DICTIONARY

dictionary = {
    'name': 'Ivan',
    'age': 19
}

dictionary['bio'] = 'gamer'
del dictionary['bio']
dictionary['bio'] = 'мамкин синок'
# print(dictionary['age'])


# for obj in dictionary:
#     print(obj, dictionary[obj])


# #! list

# list_of_numbers = [1,2,3,4,5,6]
# list_of_numbers += [1,2,3,4,5,6]

# list_of_numbers.append(10)
# list_of_numbers.pop()
# print(list_of_numbers)
# print(list_of_numbers[0:2])

# for item in list_of_numbers:
#     print(item)

# a = True
# while a == True:
#     print(list_of_numbers)
#     a = False
# else :
#     print('fuck')

# a = 5
# if a == 2:
#     print('hi')
# elif a % 2 != 0 :
#     print('ye boy')
# else:
#     print('cyka')

# a = 'a'
# b = 'b'
# c = 'a' 'b'
# print(c)
# print(a + b)
# name ='vanya'
# age = '19'
# p9dok = 'Hi, my name is {0}, I am {1} years old'.format(name, age)
# p9dok = 'Hi, my name is ' + name + ' I am ' + age + ' years old'
# print(p9dok)


def full_name(first_name, last_name):
    # print(first_name + ' ' + last_name)
    return first_name + ' ' + last_name
# full_name("Ivan", "Malashenko")
# print(full_name("Ivan", "Malashenko"))

name = full_name("Ivan", "Malashenko")
print(name)


# def f (a):
#     if a == 1:
#         print(a)
# else:
#     print(a)
# f(2)

import requests
URL = "https://jsonplaceholder.typicode.com/users"
g = requests.get(URL)
print(g.text)