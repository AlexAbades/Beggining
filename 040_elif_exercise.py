is_male = True
is_tall = False

if is_male and is_tall :
    print("You're a tall man")
elif is_male and not(is_tall):
    print("You're a small man")
elif is_tall and not(is_male):
    print("you're tall, but not a man")
else:
    print("You're not a man neither tall")