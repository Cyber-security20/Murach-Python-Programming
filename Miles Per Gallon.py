# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t"))

# calculate miles per gallon
mpg = round((miles_driven/gallons_used), 1)
total_gas_cost = round((gallons_used * cost_per_gallon), 1)
cost_per_mile = round((total_gas_cost/miles_driven), 1)
# mpg = miles_driven / gallons_used
# mpg = round(mpg, 2)

# format and display the result
print(f"\nMiles Per Gallon:\t\t{mpg}"
      f"\nTotal Gas Cost:\t\t\t{total_gas_cost}"
      f"\nCost per mile:\t\t\t{cost_per_mile}")
print("\nBye!")
