class Person():
    def __init__(self, id, name, gend, dob):
        self.__id = id
        self.__name = name
        self.__gend = gend
        self.__dob = dob
        self.__phone = "_"
        self.__email = "_"

    # Get Methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_gend(self):
        return self.__gend

    def get_dob(self):
        return self.__dob

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    # Set Methods
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_gend(self, gend):
        self.__gend = gend

    def set_dob(self, dob):
        self.__dob = dob

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

class Employee(Person):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__salary = 0
        self.__dept = "_"

    def get_salary(self):
        return self.__salary

    def get_dept(self):
        return self.__dept

    def set_salary(self, salary):
        self.__salary = salary

    def set_dept(self, dept):
        self.__dept = dept

class Doctor(Employee):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__IsMedical = True

    def IsMedical(self):
        return self.__IsMedical

class Worker(Employee):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__IsMedical = False

    def IsMedical(self):
        return self.__IsMedical

class Patient(Person):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__illness = "_"
        self.__debt = 0

    def get_illness(self):
        return self.__illness

    def get_debt(self):
        return self.__debt
    
    def set_illness(self, illness: str):
        self.__illness = illness

    def set_debt(self, debt):
        self.__debt = debt
