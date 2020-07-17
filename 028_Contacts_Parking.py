for number in range(1000):
    if number <10:
        print("00" + str(number) + "_Parking")
    elif 100 > number and number >=10:
        print("0" + str(number) + "_Parking")
    else:
        print(str(number) + "_Parking")