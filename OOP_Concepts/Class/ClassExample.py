class Example:
        # Represent Example
    def __init__(self,_name,_age,_address):
        self.name =  _name
        self.age = _age
        self.address = _address 
    # get name 
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    # behavior
    def show(self):
        print("This is Show case ")

# pass data on Example
myExample = Example("Python",199)
print(myExample.get_age())