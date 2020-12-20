text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
text2 = text[pos+1:]
fnum = float(text2)
print(fnum)