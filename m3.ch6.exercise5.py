import string

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos + 2:]
value = float(piece)

print(str)
print(ipos)
print(piece)
print(value)
