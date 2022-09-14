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
width = num_check("width: ")
height = num_check("height: ")
print()
print("Width", width)
print("height", height)
print()