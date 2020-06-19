text = "X-DSPAM-Confidence:    0.8475";

pos = text.find('0')

str = text[23:]

print(float(str))
