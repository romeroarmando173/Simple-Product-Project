class Product:

    def __init__(self,name,price,category): #cual es la idea aqui? porque podemos poner mas atributos aqui 
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased=True): #this updates the products price. THIS METHOD IS WORKIGN
        if is_increased == True:
            self.price = self.price + self.price * percent_change # does percentage_change need a self?
        else:
            self.price = self.price - self.price * percent_change #make sure you indent after else, like here
        return self

                                                    #
                                                    #print_info(self) - print the name of the product, its category, and its price.



                                                    # def print_info(self):   
                                                    #     print(self.product1= , self.category= , self.price=)
                                                                                        #  print the name of the product, its category, and its price. 
        
                
