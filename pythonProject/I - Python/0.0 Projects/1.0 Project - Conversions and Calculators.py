# Weight converter(lbs/kgs) using if statements:

Weight = float(input("How much do you weigh? "))
Unit = input("(K)g or (L)bs? ")
if Unit.upper() == "K":
    converted = Weight / 0.45
    print("Your weight in Lbs is: ", str(converted))
if Unit.upper() == "L":
    converted = Weight * 0.45
    print("You weight in Kgs is: ", str(converted))





# Energy to Mass Conversion:
c_meters_per_sec = 299792458                           # Speed of light (m/s)
joules_per_AA_battery = 4320.5                         # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.1984e9

mass_kg = float(input("\n-To be converted into energy\nWhat is the mass in kilograms: "))

    # Compute E = mc^2
energy_joules = mass_kg * (c_meters_per_sec**2)        # E = mc^2
print("Total energy released: "+str(energy_joules)+"Joules")

    # Calculate equivalent number of AA and tons of TNT
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_ton = energy_joules / joules_per_TNT_ton

print("Which is as much energy as: ")
print(" ", str(num_AA_batteries), "AA batteries")
print(" ", str(num_TNT_ton), "tons of TNT")





# Leasing Calculator - computes total cost of leasing a car

down_payment = int(input("\nCalculate Lease payment:\nEnter down payment: "))
payment_per_month = int(input("Enter monthly payment: "))
num_months = int(input("Enter number of months: "))

total_cost = down_payment + (payment_per_month * num_months)
print(f'\nTotal cost to be paid: ${total_cost:.2f}')





# Sphere-Volume Calculator:

pi = 3.14159
sphere_volume = 0.0

sphere_radius = float(input("\nTo calcualte Sphere's volume:\nWhat is the sphere's raduis: "))
sphere_volume = (4.0 / 3.0) * pi * sphere_radius**3

print(f'\nSphere volume: {sphere_volume}')





# Acceleration of Gravity Calculator:

G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

dist_center = float(input("\n-To calculate Acceleration:\nWhat is the distance to the center: "))
accel_gravity = (G * M) / dist_center**2

print(f"\nAcceleration of gravity: {accel_gravity:.2f}")






# Minutes to Hours Converter:
minutes = int(input("\n-To convert mintues into hours:\nEnter minutes:\n"))
hours = minutes // 60
minutes_remaining = minutes % 60

print(f"\n{minutes} minute(s) is {hours} hour(s) and {minutes_remaining} minute(s)")






# Even or Odd:
inp_num = int(input("Enter a number: "))

if num_months == 0:
    print(inp_num, "is even")
elif inp_num % 2==0:
    print(inp_num, " / 2 gives a remainder of ", (inp_num%2), "so it's even")
else:
    print(inp_num, " / 2 gives a remainder of ", (inp_num%2), "so it's odd")






# Divider using higher order function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)                 # assigns 2 to divisor; y = 10 and x = 2
print(divide(10))                   # assigns 10 to dividend(x)