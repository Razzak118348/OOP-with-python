class student:
    # attribute=>data of class
    college_name="Amader college"

   # parameter constructor
        # method=>function of class
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value

        print("length of marks array is :",len(self.marks))
        print('Hi', self.name, "your average marks is : ",sum/len(self.marks))



s1=student('John',[99,98,97])
s1.get_avg()

print("YOUR COLLEGE IS :",s1.college_name)
# print(student.college_name)
# both are same but the difference is that s2 is object of student class and student is a class name