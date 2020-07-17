library = [
    ["o", "m", "with", "come"]
]

def change_word(phrase):
    translation= ""
    for word in phrase:
        if word in library:
            translation = translation + "G"
        else:
            translation = translation + word
    return translation

print(change_word(input("Tell me a story: ")))

#The problem here is that we are cheking letter bi letter, beacasue with the for loop we are cheking index by index.
#and also we can't check if the wordo is in the library