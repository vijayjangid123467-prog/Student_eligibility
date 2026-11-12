marks=float(input("Enter marks out of 100:"))
att=float(input("Enter attendence in percentage:"))

if marks>=40 and att>=75:
    print("Eligible")
elif marks>=40 or att>=75:
    print("Not eligible")
else:
    print("Not eligible")