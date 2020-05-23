# Read file and print contents in upper case

filename = input('Enter name of the file to open: ')
file = open(filename)

for line in file:
    line = line.rstrip()
    print(line.upper())