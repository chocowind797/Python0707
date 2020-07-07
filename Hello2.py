h = float(input('Input your height(cm):'))
w = float(input('Input your weight(kg):'))

bmi = w / (h/100)**2

print("Your BMI is {:.4}".format(bmi))

if bmi >= 23:
    print("Too fat.")
elif 18 <= bmi < 23:
    print("Normal")
else:
    print("Too thin.")
