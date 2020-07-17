def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":  #We can check if the letter is inside of a string
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else :
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

