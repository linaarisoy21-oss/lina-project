# Take input for number of units consumed from the user
units = int(input("Please enter the Number of Units you consumed : "))

# Check conditions of units consumed
# Then calculate amount and subcharge accordingly
# subcharge is the tax value

if(units < 50): # Check for units less than 50
    amount = units * 2.60
    subcharge = 25

elif(units <= 100): # Check for units less than 100
    amount = 130 + ((units-50) * 3.25)
    subcharge = 35

elif(units <= 200): # Check for units less than or equal to 200
    amount = 130 + 162.50 + ((units-100) * 5.26)
    subcharge = 45

# Check for all the cases other than mentioned
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    subcharge = 75

# calculate and display the total electricty bill
# total amount = amount + subcharge
total = amount + subcharge
print(f"Electricity Bill = {total}")