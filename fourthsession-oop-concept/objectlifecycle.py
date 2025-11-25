class FirstCounterClassInPython:
    def __init__(self):
        self.x = 0
        print('Contructed')

    def counter(self) :
        self.x = self.x + 1
        print('My Counter now is:', self.x)

    def __del__(self) :
        print('Object released with variable :', self.x)    

fccp = FirstCounterClassInPython()
fccp.counter()
fccp.counter()

fccp = 32
print('new value of the constructor is:', fccp)
