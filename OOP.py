class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
            return f"{self.brand} {self.model} is making a call..."
        
    def charge(self):
            return f"{self.brand} {self.model} is charging..."
        
        # objects
phone1 = Smartphone("Sumsung", "Galaxy A05")
phone2 = Smartphone("Apple", "iphone 12")
print(phone1.brand, phone1.model)
print(phone1.call())
print(phone2.charge())

class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def use_feature(self):
        if self.brand.lower() == "samsung":
            return f"{self.brand} {self.model} → Using Google Assistant 🤖"
        elif self.brand.lower() == "apple":
            return f"{self.brand} {self.model} → Using Siri 🍏"
        elif self.brand.lower() == "nokia":
            return f"{self.brand} {self.model} → Using Cortana 💻"
        else:
            return f"{self.brand} {self.model} → No special assistant available ❓"


# objects
phone1 = Smartphone("Samsung", "Galaxy A05")
phone2 = Smartphone("Apple", "iPhone 12")
phone3 = Smartphone("Nokia", "Lumia 950")

# polymorphism in action
print(phone1.use_feature())
print(phone2.use_feature())
print(phone3.use_feature())
