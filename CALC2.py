what_to_measure=input("What do you want to measure? BMI/BMR-- ")
ushit=float(input("Enter your body height(m): "))
uswit=float(input("Enter your body weight(KG): "))
usage=int(input("Enter your age(Year): "))
class BMI():
    def __init__(self,bodyheight,bodyweight):
        self.height=bodyheight
        self.weight=bodyweight

    def PrintBMI(self):
        print(f"Your calculated BMI is {self.weight / self.height ** 2}")

class BMR(BMI):
    def __init__(self,bodyheight,bodyweight,age):
        super().__init__(bodyheight,bodyweight)
        self.age=age

    def PrintBMRboy(self):
        print(f"Your calculated BMR is {66 + (13.7 * self.weight) + (5 * (self.height*100)) - (6.8 * self.age)} cal")

    def PrintBMRgirl(self):
        print(f"Your calculated BMR is {655 + (9.6 * self.weight) + (1.8 * (self.height*100)) - (4.7 * self.age)} cal")

BMIuser=BMI(ushit,uswit)
BMRuser=BMR(ushit,uswit,usage)


if what_to_measure == "BMI":
    BMRuser.PrintBMI()

elif what_to_measure == "BMR":
    bog=input("Are you a Boy(B) or Girl(G)? -")
    if bog == "B":
        BMRuser.PrintBMRboy()
    else:
        BMRuser.PrintBMRgirl()

else:
    print("Invilid Input.")