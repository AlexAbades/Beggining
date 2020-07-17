secret_word = "giraffe"
guess = ""
guess_counter = 0
guess_limit = 10
clue_1 = 3
clue_2 = 6
clue_3 = 9
out_of_guesses = False
def_counter = 0

#==========================================================
#FUNCTION
#==========================================================
def clue ():
    global def_counter #If we use a variable inside of a function that we've declared outside of that function,  we have to that that variable is global.
    clue = "yes"
    fisrt_clue = "It's an animal"
    second_clue = "It lives in africa"
    third_clue = "Is yellow with black spots "
    if clue_resp.lower() == clue:
        if def_counter == 0:
            print("Okei! Here's your first clue... " + fisrt_clue )
            def_counter = def_counter + 1
        elif def_counter == 1:
            print("Okei, you're almost there! Here's your second clue... " + second_clue)
            def_counter = def_counter + 1
        elif def_counter == 2:
            print("This is your last clue, don't waste it" + third_clue)
    else:
        print("HAHAHA, come on... don't be a bad looser!")

print("Lets play a game!, I spy with my little eye something that beginning with... G!")
input("Press enter to start playing...")
print(" ")
#====================================================================================================
#MAIN CODE
#I don't now if i can put the counter inside the first loop and then don't put it inside of all the if
#====================================================================================================
while guess != secret_word and not(out_of_guesses):
    if guess_counter < clue_1:
        guess = input("Guess what i'm thinking: ")
        guess_counter += 1
    elif guess_counter == clue_1 :
        clue_resp = input("Do you want another clue? (yes/no)")
        clue()
        guess = input("Guess again: ")
        guess_counter += 1
    elif guess_counter > clue_1 and guess_counter < clue_2 :
        input("Guess again: ")
        guess_counter += 1
    elif guess_counter == clue_2 :
       clue_resp = input("Do you want another clue? (yes/no)")
       clue()
       guess = input("You're not good at this game man..., guess again: ")
       guess_counter += 1
    elif guess_counter < clue_3:
        guess = input("Guess again: ")
        guess_counter += 1
    elif guess_counter >= clue_3 and guess_counter < guess_limit:
        clue_resp = input("Okei, it's your last chance, would you like a final clue? ")
        clue()
        guess = input("If you miss you lose... Try to guess it: ")
        guess_counter += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Loser! ")
else:
    print("Winer")