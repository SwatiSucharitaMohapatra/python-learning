class StudentSMark:

    def __init__(self, name):
        self.marks = 0
        self.name = name
        print(self.name, "Constructed")

    def passmark(self) :
        self.marks = self.marks + 30
        print(self.name, 'Passmark is', self.marks)

class StudentsPassed(StudentSMark):

    def __init__(self, name):
        super().__init__(name)
        self.totalmarks = 30

    def totalpassmark(self):
        self.totalmarks = self.totalmarks + self.marks
        self.passmark()
        print(self.name, "Passed! Total Marks secured is:", self.totalmarks)

student1 = StudentSMark("Tina")
student1.passmark()

student2 = StudentsPassed('Ruby')
student2.passmark()
student2.totalpassmark()



