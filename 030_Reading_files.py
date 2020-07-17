#We can read some documents with python.
#this "open" function it only allow us to open the file.
"""
open("employees.txt", "r")
"""
#If it's in the same directory, we'll only have to specify the name of the file, but if it isn't in the same directory,
#we'll have to specify the relative path to the file or the absolute path to the file.
#The Mode, the second parameter of the function, it allow us to read (r), write (w), append (a), or read and write (r+)
#If we want to do something with the file, we have to store it into a variable

#employees_file = open("employees.txt", "r")

#print(employees_file.readline())
#print(employees_file.readline())
#print(employees_file.readline())
#print(employees_file.readline())

#employees_file.close()


employee_file = open("employees.txt", "r")
emplyee_list = employee_file.readlines()
for employee in emplyee_list:
    print(employee)
employee_file.close()
