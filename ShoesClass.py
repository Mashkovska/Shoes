class Shoes:
    total_price = 0

    def __init__(self, type_of_shoes="boots", producer="Turkey", price_by_pair=344):
         self.type_of_shoes = type_of_shoes
         self.producer = producer
         self.price_by_pair = price_by_pair
         Shoes.total_price += price_by_pair

    def to_string(self):
        print("Type of shoes: "+self.type_of_shoes+"; Producer: ",self.producer+"; price_by_pair:",self.price_by_pair)

    def print_sum(self):
        print("Price of "+str(self.type_of_shoes)+" "+ str(self.price_by_pair))

    @staticmethod
    def print_static_sum():
        print("Total price of shoes is "+str(Shoes.total_price))


if __name__=='__main__':
    boots = Shoes()
    sandals = Shoes("Sandals", "Norway", 677)
    moccasins = Shoes("Moccasins", "Ukraine", 984)

    print("\n")
    boots.to_string()
    sandals.to_string()
    moccasins.to_string()

    print("\n")
    boots.print_sum()
    sandals.print_sum()
    moccasins.print_sum()
    Shoes.print_static_sum()





