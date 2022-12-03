class Student:
    name = "Mark"
    class_attributes_out_here = "Afraid of dogs"

    def __init__(self, age):
        self.age = age
        self.isnstance_attributes_in_here = "2 legs"


    def double_age(self) -> "int":
        self.age = self.age * 2
        return self.age


    @classmethod
    def to_string(cls):
        print('Student Class Attributes: name=', cls.name)

    @classmethod
    def set_default(cls):
        cls.name = "John Smith"
        cls.class_attributes_out_here = "Forced to Default"

    @classmethod
    def set_alternative(cls):
        cls.name = "Barnaby"
        cls.class_attributes_out_here = "Special Things"


if __name__ == '__main__':

    Student.to_string()

    student = Student(age = 13)

    print()
