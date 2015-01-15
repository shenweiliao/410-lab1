class Student:
    courseMarks = {}
    name = ""
    family = ""

    def __init__(self, name, family):
        self.name = name
        self.family = family

    # note that this overwrites old course marks if they already exist
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        marks = self.courseMarks.values()
        return sum(marks)/len(marks)

if __name__ == "__main__":
    a = Student("hello", "there")
    print(a.name)
    print(a.family)
    a.addCourseMark("muh course", 1.0)
    print(a.average())
    a.addCourseMark("muh course2", 2.0)
    print(a.average())
    a.addCourseMark("muh course3", 3.0)
    print(a.average())
    b = Student("helol", "theer")
    print(b.name)
    print(b.family)
    print(b.average)
