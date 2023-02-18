import math
#This program will ask the user to choose between a bond or investment calculator.
#For investment it will calculate either simple or compound interest.
#For bond it will calculate the monthly repayment.
#An error message will be displayed if the user inputs in any choice outside of 'investment' or 'bond'

#Presenting the choice of calculation type to the user.
print("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n\n"
      "investment - to calculate the amount of interest you'll earn on your investment"
      "\nbond - to calculate the amount you'll have to pay on a home loan")

# create variable for calculation type choice.
calc_type = (input("\nEnter here:")).lower()

# create if statement for 'investment' - requesting deposit amount, interest rate, plan term and interest type.
# deposit amount converted to float and round to 2 decimal places.
# interest rate divided by 100 to get decimal equivalent.
# plan term converted to integer.
if calc_type == "investment":
    deposit_amount = float(input("How much money are you depositing: R"))
    deposit_amount = round(deposit_amount, 2)

    interest_rate = float(input("What is the interest rate (enter numbers only and don't include '%' sign):"))
    interest_rate = interest_rate / 100

    plan_term = int(input("How long is your investment plan (years):"))

    interest_type = (input("Please enter whether you want 'simple' or 'compound' interest on your plan:")).lower()

# created new if, elif and else statement within 'investment' if statement to separate calc between 'simple' and 'compound' and if invalid option chosen.
# ensured to round outcome of equations to nearest 2 decimal places.
    if interest_type == "simple":
        total_with_interest = deposit_amount * (1 + interest_rate * plan_term)
        total_with_interest = round(total_with_interest, 2)
        print(f"\nYour return of investment after {plan_term} years will be: R{total_with_interest}")

    elif interest_type == "compound":
        total_with_interest = deposit_amount * math.pow((1 + interest_rate), plan_term)
        total_with_interest = round(total_with_interest, 2)
        print(f"\nYour return of investment after {plan_term} years will be: R{total_with_interest}")

    else:
        print("\nError: Your input wasn't valid, please restart the program and try again.")

# created elif statement for 'bond' category.
# asks for property value, interest rate, plan term and calcs monthly repayment.
# property value converted to integer.
# interest rate converted to float, divided by 100 (to get decimal equivalent of %) and divide by 12 to get monthly interest as per equation.
# plan term converted to integer.
# monthly repayment equation outcome rounded to 2 decimal places.
elif calc_type == "bond":
    property_value = int(input("what is the current value of the property you are purchasing: R"))

    interest_rate = float(input("What is the interest rate (enter numbers only and don't include '%' sign):"))
    interest_rate = interest_rate / 100
    interest_rate = interest_rate / 12

    plan_term = int(input("In how many months would you like to repay the bond:"))

    monthly_payment = (interest_rate * property_value) / (1 - (1 + interest_rate) ** (-plan_term))
    monthly_payment = round(monthly_payment, 2)

    print(f"\nYour monthly repayment amount will be: R{monthly_payment}")

#else statement to output error message if anything other than investment or bond is inputted at start.
else:
    print("\nError: Your input wasn't valid, please restart the program and try again.")