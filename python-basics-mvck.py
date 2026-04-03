name=input("Enter the Name")
age=int(input("Enter ur age"))
height=float(input("Enter ur height"))
student=int(input(" if your student enter 1 else 0"))
print("Name : ",name,"| AGE : ",age,"| Height : ",height,": Student : ", "is_student" if student==1 else "not student")
age_in_months=age*12
print("age in months : ",age_in_months)
age_in_days=age*365
print("age in days : ",age_in_days)

reminde=age%7
print("reminder when age is divided by 7 : ",reminde)
age_power=age**2
print("age raised to the power 2 : ",age_power)