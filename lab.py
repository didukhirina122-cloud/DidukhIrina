class Human:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def input_data(self):
        self.name = input("Ім'я: ")
        self.age = int(input("Вік: "))

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")

    def is_adult(self):
        return self.age >= 18


class Student(Human):
    def __init__(self, name="", age=0, course=1):
        super().__init__(name, age)
        self.__course = course  # інкапсуляція

    def input_data(self):
        super().input_data()
        self.__course = int(input("Курс: "))

    def info(self):  # поліморфізм
        super().info()
        print(f"Курс: {self.__course}")


student = Student()
student.input_data()
student.info()

if student.is_adult():
    print("Повнолітній")
else:
    print("Неповнолітній")
