class ProductInfo:
    def __init__(self,name,model,price,ram,ssd,anyDiscount):
        self.name = name
        self.model = model
        self.price = price
        self.ram = ram
        self.ssd = ssd
        self.anyDiscount = anyDiscount

    def ProductDetails(self):
        print('Product name: ', self.name)
        print('Product Model: ', self.model)
        print('Product price: ', self.price)
        print('Product ssd: ', self.ssd)
        print('Product have any discount?: ', self.anyDiscount)
        return "Program End"
HP= ProductInfo("HP ","G6 840",10002,"16gv",512,False)
Lenevo= ProductInfo("Lenovo ","G6 840",10002,"16gv",1000,True)
print(HP.ProductDetails())
print(Lenevo.ProductDetails())

# to samando?