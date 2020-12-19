def computepay(h, r):
    if h <= 40 :
        return h*r
    else :
        return (40*r + (h-40)*r)

hours = float(input("Enter hours:"))
rate = float(input("Enter rate :"))
pay = computepay(hours, rate)
print("Pay", pay)