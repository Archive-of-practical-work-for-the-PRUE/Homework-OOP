class Employee():
    # Статический член 
    count = 0

    def __init__(self, organization, position, experience, name, gender, age, salary):
        self.__organization = organization
        self.__position = position
        self.__experience = experience
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__salary = salary
        self.__wallet = 0
        Employee.count += 1

    def get_organization(self):
        return self.__organization
    
    def get_position(self):
        return self.__position
    
    def get_experience(self):
        return self.__experience
    
    def get_salary(self):
        return self.__salary
    
    def get_name(self):
        return self.__name
    
    def get_gender(self):
        return self.__gender

    def get_wallet(self):
        return self.__wallet

    # Получение информации о месте работы, занимаемой должности, стаже работы, заработной плате
    def get_postion_info(self):
        return f"Организация: {self.get_organization()}\nДолжность: {self.get_position()}\nСтаж: {self.get_organization()}\nЗарплата: {self.get_salary()}"
    
    # Вывод личных данных
    def get_personal_info(self):
        return f"Полное имя: {self.get_name()}\nПол:{self.get_gender()}"
        
    # Изменение должности
    def set_position(self, position):
        self.__position = position

    # Начисление заработной платы
    def set_wallet(self):
        self.__wallet += self.__salary

    # Сравнение
    def __eq__(self, other):
        return self.__name == other.__name and self.__organization == other.__organization

    # Статический метод получения количества сотрудников
    @staticmethod
    def get_count_employees():
        return Employee.count

emp1 = Employee("Google", "Software Engineer", 5.0, "John Doe", "M", 30, 100000.0)
emp2 = Employee("Yandex", "QA", 2.0, "Alex Kirs", "M", 20, 105000.0)

print(Employee.get_count_employees())
print("----------")
print(emp1.get_postion_info())
print("----------")
print(emp1.get_personal_info())
emp1.set_position("QA")
print("----------")
print(emp1.get_postion_info())
print("----------")
print(emp1.get_wallet())
print("----------")
emp1.set_wallet()
print(emp1.get_wallet())
print("----------")
print(emp1 == emp2)