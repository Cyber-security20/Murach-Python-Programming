more = "y"

while more.lower() == "y":
    miles_driven_input = input("Enter in the miles driven: \n")
    if miles_driven_input == "":
        print("Miles driven cannot be empty. Try again\n")
        continue

    gallon_used_input = input("Enter Gallons of gas used: \n")
    if gallon_used_input == "":
        print("Miles driven be empty. Try again\n")
        continue

    try:
        miles_driven = float(miles_driven_input)
        gallons_used = float(gallon_used_input)

    except ValueError:
        print("Both entries must be valid numbers.\nTry again\n")
        break

    # except Exception as ValueError:
    #    print("Both entries must be valid numbers.\n Try again\n")

    if miles_driven <= 0 or gallons_used <= 0:
        print("Both entries must be greater than zero.\nTry again\n")
        continue

    mpg = round(miles_driven / gallons_used, 2)
    print(f"Miles per Gallon: {str(mpg)}\n")

    more = input("Continue (y/n): \n")
    print()

print("Okay, Bye! ")