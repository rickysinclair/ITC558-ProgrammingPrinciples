# A program that can work out the amount
# of tax to withhold from employee salaries.
#
# Salesure is a social media marketing startup. They have 10 employees working on a casual
# basis. Being a small company, Salesure do not have resources to purchase professional payroll
# software. They have hired you to write a simple Python program that can work out the amount
# of tax to withhold from their employee salaries.
#
# Employees are payed fortnightly, and because of casual nature of the job each fortnight the
# payment is different. The amount of withheld tax depends on the gross payment in each
# fortnight, and the income tax rates for the corresponding income bracket.
#
# An example of withheld tax calculation goes like this. Sam is entitled to fortnightly payment of
# $1870. To calculate income tax applicable, an estimate of Sam's annual income is needed.
# There are 52.143 weeks in a year. An estimation of annual income will therefore be $1870 ×
# 52.143 / 2 = $48,753.705 or $48,753 after rounding down. From the table, the applicable tax
# rate is 28%. Hence, the amount of tax to withhold will be 28% of $1870 = $523.60, and Sam will
# be payed an after-tax salary of $1346.40 in this fortnight.
#
# Using this method, your program will ask the user for the employee name and their gross
# fortnightly salary, and then it will work out the tax to withhold and actual salary to be payed
# out. At the end of a calculation, program would ask if user wants tax calculation of another
# employee (in which case it loop through the whole process) or finish.
#
# You do not have to handle invalid inputs (like non-numeric salary, empty name etc.). All the
# currency figures must be displayed as floating point numbers with 2 decimal places.


print("Welcome to Salesure Tax Payroll Calculator")
print("------------------------------------------")

# initialise tax rates
taxPerc5 = 0.05
taxPerc15 = 0.15
taxPerc28 = 0.28
taxPerc21 = 0.21
taxPerc13 = 0.13

# set while loop variable to true
userAns = "y"

# while loop
while (userAns == "y"):

    # prompt user for employee name
    empName = input("\nPlease enter employee name: ")

    # prompt user for gross fortnightly pay
    grossPay = float(input("Please enter gross fortnightly payment for ["
                           + empName + "]: "))

    # calculate annual income
    annualIncome = grossPay * 52.143 / 2

    # calculate tax based upon annual income level
    if (annualIncome <= 15000):
        tax = grossPay * taxPerc5
    elif (annualIncome >= 15001 and annualIncome <= 40000):
        tax = grossPay * taxPerc15
    elif (annualIncome >= 40001 and annualIncome <= 90000):
        tax = grossPay * taxPerc28
    elif (annualIncome >= 90001 and annualIncome <= 150000):
        tax = grossPay * taxPerc21
    else:
        tax = grossPay * taxPerc13

    #  calculate salary
    salary = grossPay - tax

    # display tax to withold rounded to 2 decimal places
    print(f"Amount of tax to withhold: ${tax:.2f}")

    # display salary rounded to 2 decimal places
    print("Salary payable to [" + empName + f"]: ${salary:.2f}\n")

    # prompt user to see if they wish to continue
    userAns = input("Do you want to calculate pay for another employee? (y/n): ")

# print closing message
print("Thank you. See you later.")