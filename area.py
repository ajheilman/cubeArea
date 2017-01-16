"""
The equation is 6x^2 with x representing the length of the cube
The user types in the length of the cube
It will output the answer
"""
length = raw_input("Enter the length of the cube: ")

while length.isalpha() or length >= 0 or length == "":
    print "\nYou must enter a number! Please try again!"
    length = raw_input("Enter the length of the cube: ")
    while length <= 0:
        print "\nYou must enter a positive number! Please try again!"
        #length = int(input("Enter the length of the cube: "))
        length = raw_input("Enter the length of the cube: ")
        if length >= 0:
            break
    if length.isdigit() and length != "":
        break

area = 6 * (int(length) ** 2)
print "The area of the cube is", area
