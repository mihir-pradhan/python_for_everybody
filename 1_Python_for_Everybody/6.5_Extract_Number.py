# Extract number using find() and string slicing

text = "X-DSPAM-Confidence:    0.8475"
col_pos = text.find(':')
val =  text[col_pos+1:]
val = val.lstrip()
num = float(val)
print(num)