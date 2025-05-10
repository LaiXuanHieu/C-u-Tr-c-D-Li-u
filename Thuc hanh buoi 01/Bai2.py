class Person:
    def __init__(self, name, yob):
        self.name = name.strip()
        self.yob = yob

    def describe(self):
        print(f"{self.__class__.__name__} - Name: {self.name} - YoB: {self.yob}")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade.strip()

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject.strip()

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist.strip()

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name.strip()
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = [person.yob for person in self.people if isinstance(person, Teacher)]
        return sum(teachers) / len(teachers) if teachers else 0


# Example 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1980, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1976, specialist="Endocrinologists")
doctor1.describe()

# Example 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=2003, subject="History")
doctor2 = Doctor(name="doctorB", yob=1985, specialist="Cardiologists")
ward1 = Ward(name="Ward1")

ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# Example 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# Example 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# Example 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
