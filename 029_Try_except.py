#with this function we can except some kind of error, if we don't specify what kind of error er will allow all of them
#1
#number = int(input("Enter a name: ")) # int=we are saying that the input of the user it would be a integer, number 1,2,3,4,5,6
#print(number)

#If the user enter a string or a decimal number the code will crash
#so with the finality of protect our code, we're going to put an try/except function
"""
try:
    number = int(input("Enter a name: "))
    print(number)
except:
    print("Invalid action 0")
"""
#Take atention to, the colons after try and expect!
#Also take atention that after the except we have to print something, if we don't print what action has to do after the except expression it would pit en error

#The problem is that if want only to allow a type of error, this expresion is so generalized, so we have to specfify a little bit more
"""
try:
    value = 10/0 #this is not possible
    number1 = int(input("Enter a name: "))
    print(number)
except:
    print("Invalid action 1")
#In this situation, we won't even have the posibilty to enter nothing, as the value variable it's not posible it would spit the ecxept message
"""
try:
    value1 = 10/0
    number2 = int(input("Enter a name: "))
    print(number2)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Not a number")

#we also can store as a variable,

try:
    value2 = 10/0
    number3 = int(input("Enter a name"))
    print(number3)
except ZeroDivisionError as err:
    print(err)
except ValueError as err2:
    print(err2)