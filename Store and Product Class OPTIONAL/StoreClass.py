from productClass import *          #importing productClass into this class

class Store: 
    def __init__ (self, name): #here you a
        self.name = name           #you can also crate as many stores as you want
        self.productList = []
   
    def add_product(self, new_product):
        self.productList.append(new_product)  #append is the push for python//takes a product and adds it to the store. addin to the array

    def printProds(self):
        for p in self.productList: # we are creating a for loop/ we grabbed the productList from above
            print(p.name,p.price, p.category) #this name is from the product list class at the very top where __init__ is

    def sell_product(self,id):    # BASICALLY I STOPPED HERE BECAUSE THIS IS OTPIONAL BUT WILL COME BACK TO THIS IF I HAVE TIME
        
                                        # sell_product(self, id) - remove the product from the store's list of products given the id 
                                                           # (assume id is the index of the product in the list) and print its info.
            
                                        


store1 = Store("WholeFoods")
store1.name = "WholeFoods"
product1 = Product('banana_yellow',1,'fruit')      # dont forget to add these argumetns AND INDENTATION is IMPORTANT!!!!!!
product1.name = 'banana_yellow'
product1.price = 1
product1.category = 'fruit'

store1.add_product(product1)
store1.printProds()   #this method (printPods)is inside the Store class and so this is why its caleed "store1."
                        #this one above prints product, price and category

product1.update_price(0.3, True) #notice that we listed the object first (product1) and then the mehtod
store1.printProds()


