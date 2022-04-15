class Patient:
    def __init__(self, id, name, sex, dob, phone):
        self.__id = id
        self.__name = name
        self.__sex = sex
        self.__dob = dob
        self.__phone = phone
        self.__debt = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_dob(self):
        return self.__dob

    def get_phone(self):
        return self.__phone

    def get_debt(self):
        return self.__debt