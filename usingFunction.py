def computepay(h,r):
    if h > 40 :
        pay = 40 * r + (h - 40)*1.5 * r
    else :
        pay = h * r
    return pay

hours = input("Enter Hours:")
hrs = float(hours)

rate = input("Enter rate per Hour:")
rte = float(rate)

p = computepay(hrs,rte)
print("Pay",p)
