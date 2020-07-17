for number in range(70):
    if number <10:
        print("00" + str(number) + "_Corts,")
    elif 100 > number and number >=10:
        print("0" + str(number) + "_Corts,")
    else:
        print(str(number) + "_Corts,")