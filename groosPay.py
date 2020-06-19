hours = input("Enter Hours:")
hrs = float(hours)

rate = input("Enter rate per hour:")
rte = float(rate)

if hours > 40 :
    pay = 40 * rte +(rte * 1.5 * (hrs-40));
    print(pay)

else:
    pay = hrs * rte
    print(pay)
