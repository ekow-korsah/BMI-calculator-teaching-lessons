# BMI = (weight in pounds x 703) / (Height in inches x height in inches)

#create input for the user first
#first thing you need to calculate is their weight

## Criteria
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

if BMI > 0:
    if BMI < 18.5:
        print("Hey " + name + ", you are underweight")
    elif BMI <= 24.9:
        print("Hey " + name + ", you are Normal weight")
    elif BMI <= 29.9:
        print("Hey " + name + ", you are Overweight")
    elif BMI <= 30:
        print("Hey " + name + ", you are Obese")
    else:
        print("Hey " + name + ", you are extremely Obese")
else:
    print("Hey " + name + ", you entered the wrong input")

