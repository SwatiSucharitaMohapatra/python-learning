
# Function to compute gross pay
def computepay(hours, rate) :
    if hours < 0:
        print('Enter a valid value')
        quit()
    elif hours <= 40 :
        grosspay = hours * rate
        return grosspay
    else :
        grosspay = (frate * 40) + ((hours-40) * rate * 1.5)
        return grosspay


hrs = input('Enter Hours:')
rate = input ('Enter rate per Hours:')
try:
    fhours = float(hrs)
    frate = float(rate)
except:
    print("Error, Please enter correct values")
    quit()
print("Pay", computepay(fhours, frate))