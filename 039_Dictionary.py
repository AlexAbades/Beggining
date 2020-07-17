print("Special structures in python that allows us to \n store information in what it's called a \n "
      "key value pair, so essentially I can just create \n a bunch of these different key value pairs")
print("Key words at the left, Values et the right. \n The key words must be uniques. They can't be repeated ")
print(" \n ")
print("EXAMPLE")
monthsConvertions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print("Way one to get values from the key words of a dictionary: (Look the code)")
print(monthsConvertions["May"])
print(" ")
print("Way two to get information from kay word of a dictionary, and also pass a default value: (Again, look the code)")
print((monthsConvertions.get("Dbc", "Invalid key word")))
print(" \n ")
print("The key words hasn't to be strings, they can be also numbers.")