# Calculate Pay - Regular pay for up to 40 hours and 1.5 times pay for all hours above 40 hours

hours = input("Enter Hours: ")
rate = input("Enter pay rate: ")

hours = float(hours)
rate = float(rate)

if (hours <= 40):
    pay = hours * rate
else:
    regular_pay = rate * 40
    overtime_hours = hours - 40
    overtime_rate = rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
    pay = regular_pay + overtime_pay

print(pay)