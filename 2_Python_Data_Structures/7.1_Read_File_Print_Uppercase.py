# Read file and print contents in upper case

filename = input('Enter name of the file to open: ')
file = open(filename)
readfile = file.read()
readfile = readfile.rstrip()
file_up = readfile.upper()
print(file_up)