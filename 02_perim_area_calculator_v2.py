# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number more than zero"

        try:

            # ask user to enter a number 
            response = float(input(question))
    
            # checks if number is more than zero
            if response > 0:
                return response
    
            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)



# Main routine goes here

# introduction / heading print statements
print()
print("**** Area Perimeter Calculator ****")
print ()

# start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # calculate area (width x height)
    area = width * height

    # calculate perimeter (width + height) x 2 
    perimeter = 2 * (width + height)

    # output area and perimeter
    print("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format(area))


    keep_going = input("press <enter> to keep going or any key to quit ")

print()
print("Thanks for using the area / perimeter calculator")