class Person:
  def __init__(self,_name,_age,_adress):
    self.name = _name
    self.age = _age
    self.adress = _adress
  def details(self):
    print(f"Name: {self.name}\nAge: {self.age}\nAdress: {self.adress}")
    return "End"

Person1 = Person("John",25,"123 Main St")
Person2 = Person("Jane",30,"456 Elm St")
Person3 = Person("Hamid",23,"789 Oak St")

print(Person1.details())
print(Person2.details())
print(Person3.details())
