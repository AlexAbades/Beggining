#We want to create a funcion that makes the first number to the exponent of other using the for loop!
#We need two numbers, and the idea is multiplicate the second number of times the fisrt number.

def raise_to_the_power(num_1, num_2): #Remmember, the numbers, or the elements between the parentheses are called parameters.
    result = 1
    for index in range(num_2):
        result = result * num_1
    return result

print(raise_to_the_power(2,  2))