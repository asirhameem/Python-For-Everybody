largest = None
smallest = None

while True :
    number = input("Enter Number:")

    try:
        num = int(number)
        if largest is None or largest < num :
            largest = num
        elif smallest is None or smallest > num:
            smallest = num

    except:
        if number == "done" :
            break
        print("invalid Number.")


print("Maximum is ",largest)
print("Minimum Is ",smallest)
