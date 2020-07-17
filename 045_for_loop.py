#1
for index in "Giraffe Academy":
    print(index)
print(" ")
print("NEXT FOR LOOP")
print(" ")
#2
for letter in "Giraffe Academy":
    print(letter)
#The name of the variable it really doesn't matter! Look at the two exemples.
#We change thee variable name and we made the same.
print(" ")
print("Next for loop")
print(" ")
friends = ["Kevin", "Karen", "Ari", "Roger", "Pau", "Ferran"] # The lenght of the list is the number of elements that it has.
           # 0          1       2       3       4       5       In that case, the number of elements is 6

#As we saw at the beggining of the course, in the basic functions, the ones that are already done as pow function.
#We can get printed from a list some indexes.
print(friends[2])
#3
for friend in friends:
    print(friend)
print(" ")
print("Next for loop")
print(" ")
#4
for number in range(10):
    print(number)
print(" ")
print("Next for loop")
print(" ")
#5
for name in range(len(friends)):  #Is the same function as the exercise 3
    print(friends[name])
print(" ")
print("Next for loop")
print(" ")
#6
for name in range(len(friends)):
    if name == 0:
        print("Here is your first iteration " + str(name))
    elif name != 0 and name != range(len(friends)):
        print("You still have iterations " + str(name))
    else:
        print("That's your last iteration " + str(name))




