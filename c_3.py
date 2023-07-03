class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age >= 65:
            return 1200
        elif self.age >= 20 and self.age < 65:
            return 1500
        else:
            return 1000


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す
# print(ken.entry_fee())  # 1000 という値を出力

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()  # 1500 という値を返す
# print(tom.entry_fee()) 値を出力

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()  # 1200 という値を返す
# print(ieyasu.entry_fee()) 1200という値を出力
