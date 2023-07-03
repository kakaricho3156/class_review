class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age >= 75:
            return 500
        elif self.age >= 65 and self.age < 75:
            return 1200
        elif self.age >= 20 and self.age < 65:
            return 1500
        elif self.age >= 4 and self.age < 20:
            return 1000
        else:
            return 0

    def info_csv(self):
        return f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
# print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を表示
