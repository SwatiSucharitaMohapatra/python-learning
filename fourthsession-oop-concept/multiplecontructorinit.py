class CounterClass:
    def __init__(self, name):
        self.x = 0
        self.name = name
        print('Constructor for:', self.name)

    def counter(self) :
        self.x = self.x + 1
        print('My Counter now is for', self.name, self.x) 

counterobjectsally = CounterClass("Name: Sally")
counterobjectsally.counter()

counterobjectjim = CounterClass("Name: Jim")
counterobjectjim.counter()

counterobjectsally.counter()

