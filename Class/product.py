class ProductInfo:
    def __init__(self,_name,_model,_price,_ram,_ssd,_anyDiscount):
        self.name = _name
        self.model = _model
        self.price = _price
        self.ram = _ram
        self.ssd = _ssd
        self.anyDiscount = _anyDiscount

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