is_male = False
if is_male:
    print(("You're a male"))
else:
    print("You aren't a male")
print("")
print("OR operator")
print(" ")

is_male_1 = True
is_tall_1 = True

if is_male_1 or is_tall_1:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")

print("")
print("AND operator")
print(" ")

if is_male_1 and is_tall_1:
    print("You're a tall man")
else:
    print("You're either not a male or not tall or both")