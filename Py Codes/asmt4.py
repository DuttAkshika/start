score = input("Enter Score: ")
try:
    sc = float(score)
except:
    print("Please enter a numeric value")
if sc >= 0.0 and sc <= 1.0 :
    if sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    elif sc < 0.6:
        print('F')
else : print("Please enter a value in range of 0.0 to 1.0")