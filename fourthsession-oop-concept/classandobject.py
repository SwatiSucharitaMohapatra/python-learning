class FirstCounterClassInPython:
    def __init__(self):
        self.x = 0

    def counter(self) :
        self.x = self.x + 1
        print('My Counter now is:', self.x)

fccp = FirstCounterClassInPython()

fccp.counter()
fccp.counter()
fccp.counter()

print ('Type of fccp :', type(fccp))
print ('Type of counter :', type(fccp.counter))
print ('Type of x :', type(fccp.x))
print ('Dir of Class :', dir(fccp))