hrs = float(input("Enter Hours:"))
Rt = float(input('Enter Rate'))
if hrs <= 40 :
    pay = hrs * Rt
    print(pay)
elif hrs > 40 :
    pay = (40*Rt) + (hrs-40)*1.5*Rt
    print(pay)