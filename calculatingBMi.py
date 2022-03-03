print('Calculating BMI')
weight = float(input('Please Enter Your Weight In Kilo:'))
height = float(input('Please Enter Your height In cm:'))

if(weight == 0 or height == 0):
    print('Enter Valid Number')
else:
    print('Your BMI Is', (weight/height**2)*100)