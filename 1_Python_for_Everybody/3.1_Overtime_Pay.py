# Calculate Pay - Regular pay for up to 40 hours and 1.5 times pay for all hours above 40 hours

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if (hours > 40):
    regular_pay = rate * 40
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

print("Pay:", pay)