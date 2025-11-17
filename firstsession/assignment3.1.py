
hrs = input('Enter Hours:')
rate = input ('Enter rate pe Hours:')

try:
    fhours = float(hrs)
    frate = float(rate)
except:
    print("Error, Please enter correct values")
    quit()

if fhours < 0:
    print('Enter a valid value')
elif fhours <= 40 :
    grosspay = fhours * frate
    print(grosspay)
else :
    grosspay = (frate * 40) + ((fhours-40) * frate * 1.5)
    print(grosspay)