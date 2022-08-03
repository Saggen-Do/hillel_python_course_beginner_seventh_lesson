# list comprehension first example
squares = [x ** 2 for x in range(10)]
print('list comprehension first example: ',squares)
# list comprehension second example
initial_insert = ['red', 'white', 'black', 'red', 'green', 'black']
final_list_with_no_duplicates = []
x = [final_list_with_no_duplicates.append(i) for i in initial_insert if i not in final_list_with_no_duplicates]
print('list comprehension second example: ', final_list_with_no_duplicates)
# list comprehension third example
initial_string = ('Hillel school')
result = (initial_string.lower() if 'o' not in initial_string else initial_string.upper())
print('list comprehension third example: ', result)
# list comprehension forth example
numbers_ord = [ord(str(i)) for i in range(10)]
print('list comprehension forth example: ', numbers_ord)
# list comprehension fifth example
h_letters = [letter for letter in 'human']
print('list comprehension fifth example: ',h_letters)

print()

# dict comprehension first example
simple_string = list('simple string')
character_dict = {i:simple_string.index(i) for i in simple_string}
print('dict comprehension first example: ', character_dict)
# dict comprehension second example
words = ['data', 'science', 'machine', 'learning', 'a']
word_length = {i:len(i) for i in words}
print('dict comprehension second example: ', word_length)
# dict comprehension third example
fruits = ['apple', 'plum', 'peach']
price = ['2.15', '3.45', '1.14']
to_buy = {k: v for k, v in(zip(fruits, price))}
print('dict comprehension third example: ', to_buy)
# dict comprehension forth example
import random
players = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
lottery = {customer:random.randint(1,100) for customer in players}
print('dict comprehension forth example: ',lottery)
# dict comprehension fifth example
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
temp_F = [round((i*1.8+32), 2) for i in temp_C]
days_temp_F = {x: y for(x, y) in zip(days, temp_F)}
print('dict comprehension fifth example: ', days_temp_F)

print()

# set comprehension first example
letters_list = list('letters')
letters_ord = {ord(i) for i in letters_list}
print('set comprehension first example: ', letters_ord)
# set comprehension second example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_set = {element*3 for element in my_list}
print('set comprehension second example: ', new_set)
# set comprehension third example
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = {element for element in my_set if element % 2 == 0}
print('set comprehension third example: ', even_set)
# set comprehension forth example
cooked_list = {i for i in [1, 3, 3, 5, 4, 6, 6, 7, 7, 8, 99, 11, 100, 100] if i>10}
print('set comprehension forth example: ', cooked_list)
# set comprehension fifth example
first_set = {x for x in range(1, 10, 2)}
second_set = {y for y in range(3, 15, 1)}
second_set.update(first_set)
print('set comprehension fifth example: ', second_set)