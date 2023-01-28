#Building a BMI and BMR Calculator

mes=input("What do you want to measure??: BMI/BMR")
if mes=="BMR":
    # BMR Measurement
    borg = input("Are you a boy(B) or girl(G):")

    height = float(input("Enter your Height(cm):"))
    weight = float(input("Enter your Weight(kg):"))
    age = int(input("Enter your age:"))


    def bBMR(hyt, wet, age):
        height = hyt
        weight = wet
        age = age
        print(f"Your BMR is:{66 + (13.7 * weight) + (5 * height) - (6.8 * age)} cal")


    def gBMR(hyt, wet, age):
        height = hyt
        weight = wet
        age = age
        print(f"Your BMR is:{655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)} cal")


    if borg == "B":
        bBMR(height, weight, age)
    else:
        gBMR(height, weight, age)


else:
    # BMI Mesurement
    def BMI(hight, wight):
        print(wight / hight ** 2)


    height = float(input("Enter your hight:"))
    weight = float(input("Enter your wight:"))
    BMI(height, weight)


