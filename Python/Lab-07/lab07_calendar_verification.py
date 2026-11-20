print("===============================================")
print("          CALENDAR VERIFICATION SYSTEM         ")
print("===============================================")
y=int(input("Enter year: "))

if y<=0:
    print("Error! Year must be greater than 0.")
else:
    if y % 400==0:
        leap=True
        reason="Century year divisible by 400"
    elif y % 100==0:
        leap=False
        reason="Century year not divisible by 400"
    elif y % 4==0:
        leap=True
        reason="Divisible by 4 and not a century year"
    else:
        leap=False
        reason="Not divisible by 4"

if leap==True:
    status="LEAP YEAR"
    feb_days=29
    year_days=366
else:
    status="COMMON YEAR"
    feb_days=28
    year_days=365
print(" ")
print("---------------------------------------------------")
print(f"Year: {y}")
print(f"Status: {status}")
print(f"Days in Year: {year_days}")
print(f"Days in February: {feb_days}")
print(f"Reason: {reason}")