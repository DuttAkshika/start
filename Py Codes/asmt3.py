hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try :
    h = float(hrs)
    r = float(rate)
except :
    print("Enter numeric values.")
    quit()
if h <= 40 :
    pay = h*r
else :
    pay = 40*r + (h-40)*1.5*r
print(pay)