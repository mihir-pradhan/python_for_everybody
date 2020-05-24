# Open a file, count lines starting with X-DSPAM-Confidence, extract floating point values, compute and print average

filename = input('Enter the name of file to open: ')
file = open(filename)

count = 0
x_dspam_lines = 0
for line in file:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    col_pos = line.find(':')
    num = line[col_pos+1:]
    num = float(num.strip())
    x_dspam_lines += num
    count += 1

print('Average spam confidence:', x_dspam_lines/count)