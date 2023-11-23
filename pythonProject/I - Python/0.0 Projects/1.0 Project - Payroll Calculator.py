'''
Hello! My name is Kevin Dacanay.
This is a Payroll Calculator program.
INPUT - This program will take in user (name and number of hours worked)
PROCESS - The program will then calculate the gross pay and all taxes that are deducted.
OUTPUT - The program will then give out your net pay along with income deductibles
'''

#INPUT: The program will ask the user to input their name and number of hours worked.
name = input("Hello! What is your name? ").capitalize()
print("Hello "+name+"!")

'''
The input for number of hours is in a while loop to assure correct input.
If the user inputs a string(not a number), the program will produce an error  
message and ask the user to enter a valid numerical input
'''
while True:
    try:
        hours = float(input("How many hours did you work today? (please enter a number): "))
        break
    except ValueError:
        print("Invalid! Please enter a number")

# PROCESS: The program will now then calculate your gross pay
#          along with all taxes deducted from your pay.
'''
1.	Set pay rate as a constant, $30 per hour
2.	Set Fed tax rate as a constant, 15%
3.	Set State tax rate as constant, 5%
4.	Set Social Security Tax as constant, 7%
5.	Find gross pay
6.	Find taxes
7.	Find net pay = gross pay – taxes
'''
# Listing all assigned variables for taxes and pay rate then calculating each:
pay_rate = float(input("What is your pay rate: "))
Fed_tax = 00.15
State_tax = 00.05
Social_Security_tax = 00.07

Gross_pay = hours * pay_rate
Fed_deducted = Gross_pay * Fed_tax
State_deducted = Gross_pay * State_tax
SS_deducted = Gross_pay * Social_Security_tax

# OUTPUT: The program then prints out your Net Pay along with your Taxes Deducted.
#         (Numbers are rounded)
print("Your Gross Pay is: $", round(Gross_pay,2))
print("Your Federal Tax is: $", round(Fed_deducted,2))
print("Your State Tax is: $", round(State_deducted,2))
print("Your Social Security Tax is: $", round(SS_deducted,2))

Net_pay = Gross_pay - (Fed_deducted + State_deducted + SS_deducted)
print(name+", your Net Pay is: $", round(Net_pay, 2))
