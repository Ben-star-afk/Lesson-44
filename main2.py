class student:
    grade=10
    name="Benedict"
    def introduction(self):
        print("Hi I am a student")
    def details(self):
        print("My name is:",self.name)
        print("My age is:",self.grade)
ob=student()        
ob.introduction()
ob.details()