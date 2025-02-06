wt=float(input("Enter you'r weight in kg"))
ht=float(input("Enter you'r hight in m"))
bmi=wt/(ht*ht)
print("you'r BMI is ",bmi)

if bmi<=18.5:
    print("You are underweight")
elif bmi>18.5 and bmi<=25:
    print("You are normal")
elif bmi>25 and bmi<=30:
    print("You are overweight")
elif bmi>30 and bmi<=35:
    print("You are obese")
elif bmi>35:
    print("You are Morbid Obesit")
else:
    print("Please enter valid input")