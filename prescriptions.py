class patients:
    def __init__(self, name, age, phone, doctor_name, doctor_DEAnumber, diagnosis, medicines):
        self.name = name
        self.age = age
        self.phone = phone
        self.doctor_name = doctor_name
        self.doctor_DEAnumber = doctor_DEAnumber
        self.diagnosis = diagnosis
        self.medicines = medicines
    
    def add_name(self, name):
        name = input("Member's name: ")

    def add_age(self, age):
        age = int(input("Member's age:"))

    def add_phone(self, phone):
        phone = int(input("Member's phone: "))
    
    def add_doctor_name(self, phone):
        phone = int(input("Member's doctor_name: "))

    