height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

diagnosis = ""
if bmi < 16.00:
    diagnosis = "Starvation"
elif 16.00 < bmi < 16.99:
    diagnosis = "Emaciation"
elif 17.00 < bmi < 18.49:
    diagnosis = "Underweight"
elif 18.50 < bmi < 24.99:
    diagnosis = "Correct weight"
elif 25.00 < bmi < 29.99:
    diagnosis = "Overweight"
elif 30.00 < bmi < 34.99:
    diagnosis = "First degree obesity"
elif 35.00 < bmi < 39.99:
    diagnosis = "Second degree obesity (clinical)"
else:
    diagnosis = "Third degree obesity (extreme)"

print("Your BMI is:", bmi)
print("Diagnosis:", diagnosis)
print("Correct interval for weight and height: 18.50-24.99")