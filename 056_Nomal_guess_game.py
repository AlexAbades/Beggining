secret_word = "giraffe"
guess = ""
guess_counter = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_counter < guess_limit :
        guess = input("Enter a word: ")
        guess_counter += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose")
else:
    print("You Win")
