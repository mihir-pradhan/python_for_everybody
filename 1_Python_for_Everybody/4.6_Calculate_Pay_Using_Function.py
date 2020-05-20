# Calculate overtime pay using a function

def computepay(hours, rate):
    if (hours > 40):
        regular_pay = rate * 40
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(hours, rate)
print("Pay", pay)