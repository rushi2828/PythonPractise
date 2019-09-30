# Python Strings
from audioop import reverse
from builtins import len, input, int

test = "this is Python First"

print('o/p is ----> ', test)  # o/p--->i

# Print particular character
print('o/p is ----> ', test[2])  # o/p--->This is Python First

# Print from particular character
print('o/p is ----> ', test[8:])  # o/p---> Python First

print(len(test))

print(test.upper())  # o/p---> THIS IS PYTHON FIRST

print(test.lower())  # o/p---> this is python first

print(test.capitalize())  # o/p---> This is python first
# ====================================================================
'''
Multiple lines Comments
Like this
'''

# ====================================================================
print('===================================')
# If-else statements

'''age = int(input("Enter the age"))

if age < 18:
    print('You are child')
else:
    print('Congrats You Are Adult Now')

# Example No. : 2

num = int(input('Enter the value'))
if num % 2 == 0:
    print ('Even')
else:
    print('Odd')

num = int(input('Enter the value '))
if num == 10:
    print ('The number is 10')
elif num == 20:
    print ('The number is 20')
elif num == 30:
    print ('The number is 30')
else:
    print ('The number is above 30')'''

# ====================================================================#
print('===================================')

# Loops in python
'''
SYNTAX : 

for iterating_var in sequence:  
    statement(s)  
'''

# ====================================================================#

colors = ['red', 'orange', 'pink', 'white', 'black']
for i in range(len(colors)):
    print(colors[i])

# ============================ If-Else Statement ==========================================#

print('===================================')
# x = int(input('enter the number'))

x = -1
if x < 0:
    print('Number is negative')
elif x == 0:
    print('X is Zero')
else:
    print('Number is positive')

# ============================ Python: LISTS ===============================================#
print('===================================')

words = ['a', 'this', 'new', 'word']
numbers = [2, 3, 4, 5, 7, 8, 9, 6, 23, 56, 78]

print(words[:4])

print('===================================')

print(numbers[1:5])

print('===================================')

print(list(reversed(numbers)))

print('===================================')

for w in words:
    print(w, len(w))

# ============================ OOPS CONCEPTS: Class and Objects  ===========================#
print('===================================')


# Class and objects
class FirstClass:
    id = 10
    name = "Rushi"

    def display(self):
        print(self.name, self.id)
        print("ID:%d\nName:%s" % (self.id, self.name))


firstClass = FirstClass()
firstClass.display()

# ============================ OOPS CONCEPTS: Python Constructor ===========================#
print('===================================')



