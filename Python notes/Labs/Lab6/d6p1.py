class Student:
    def __init__(self, name, age, city, roll_no, stream, college):
        self.name = name
        self.age = age
        self.city = city
        self.roll_no = roll_no
        self.stream = stream
        self.college = college

# Creating an object
s1 = Student("Bikram", 19, "Kolkata", 101, "CSE", "Heritage Institute of Technology")
print(s1.name, s1.college)
