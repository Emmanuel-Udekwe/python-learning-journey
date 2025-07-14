# BMI calculator (basic)
# ask the user for weight and height, then calculate and print BMI.
weight = float(input("enter your weight in kg:"))
height = float(input("enter your height in meters:"))
BMI = weight/(height * height)
print ("Your body mass index is:",round(BMI,2))