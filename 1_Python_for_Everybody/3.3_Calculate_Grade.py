# Calculate grade based on user input

score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Error, please enter numeric input between 0.0 and 1.0")
    quit()

if (score > 1.0 or score < 0):
    print("Error, please enter numeric input between 0.0 and 1.0")
elif (score >= 0.9):
    print("Grade A")
elif (score >= 0.8):
    print("Grade B")
elif (score >= 0.7):
    print("Grade C")
elif (score >= 0.6):
    print("Grade D")
else:
    print("Grade F")