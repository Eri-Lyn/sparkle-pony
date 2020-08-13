"""
ASSIGNMENT 3 -- ONLINE SHOPPING
````````````````````````````````````````````````````````````````````````````````````````
SUMMARY:
   We're going to be creating a fake shopping website that the user navigates via terminal. Here are
   the requirements:

   1. There must be a main menu with five options and their cart:
      a. Clothes
      b. Household Items
      c. Tools
      d. Adult Toys
      e. Throngo Jotchy
      f. -- SHOW CART --

   2. Once a user selects an option, it should print out at least five items (that you make up) that list their
      name, price, and inventory, along with a BACK option. Here's an example after someone chooses 'Clothes':
         1. -- BACK --
         2. Tanktop        $14.99      3
         3. Blue Jeans     $25.89      12
         4. T-Shirt        $19.99      5
         5. Skirt          $16.98      3
         6. Tennis Shoes   $49.99      2

   3. Once someone selects an item it should be added to their cart, and that item's inventory should decrement.

   4. If someone selects SHOW CART in the main menu, it should display everything they selected.

   5. If an item is bought out (example: buying the two tennis shoes in the above example), it should be REMOVED
      from the menu.

   6. The items should all be apart of a new class called ShoppingItem(made this ShoppingCart in my program - Eri). It should have the member variables:
      name, price, stock

If you have any questions let me know, as this is more involved. But, it uses all the stuff you've learned thus far,
like making a class and retrieving it from a list. And lots of printing and formatting. :^)
"""


### CLASSES ###


#creating ShoppingItem class - will be used to store items in dicts for 'menu' printing

class ShoppingItem:
    def __init__(self, name, price, units):
        self.name = name
        self.price = price
        self.units = units

    #print_menus function string formatting    
    def __rper__(self):
        #might be a way to make this a little prettier - i.e. aligning $'s and 'Stock' vertically.
        return '{0}: ${1}  Stock - {2}' .format(self.name, self.price, self.units)
"""
    def out_of_stock():  
    # probs don't need this and can decrement value in add_to_cart function; keeping it here just in case for now

"""

class ShoppingCart:

    def __init__(self):
       self.cart = [] #I don't think I need this list, but I think I need to add something to init

    #formatting for when user toggles Show Cart option in main menu; related to show_cart
    def __rper__(self):
        return '{0}  ${1}  {2}' .format(self.name, self.price, self.units)
    
    #when progam is more mature will have to account for units; if using add_to_cart to decrement stock this might be better as a general function?
    def add_to_cart(self, item):
        self.cart.append(item)
        
    #this is not a part of the charge; using for OOP practice and still figuring the if statement out for this
    def check_out(self):
        print(buy_cart.cart[0].price * buy_cart.cart[0].units)


#function to print all menus/dicts
def print_menus(dct):
    for key, value in dct.items():
        print("{} {}".format(key, value))

#show items in user's cart; could combine with check_out for funsies; have a feeling this might not be modular
def show_cart():
    for x in buy_cart.cart:
        print(x.__rper__())


#def greetings() ; will print an initial greeting
#def convert_to_item()
#def return_to_main()
#def show_cart()


### VARIABLES ###


buy_cart = ShoppingCart()

main_menu = { "a." : "Clothes",
              "b." : "Make-up",
              "c." : "Adult Toys",
              "d." : "Skin Care",
              "e." : "Snack Store",
              "f." : "~*~SHOW CART~*~"
              }

"""
 Clothes menu class variables and dict; will make this general header for all sub menus if idea pans out;
 Formatting for variables under ShoppingItem; idea is to take user input, convert item to shoppingcart class; make user input variable & subtract from unit
 Make sure to remove above line and put it over the actual function I'll make to acomplish user-input/ShoppingCart/unit subtraction
"""

tennis_shoe = ShoppingItem("Tennis Shoes" , 14.99 , 3)
spanx = ShoppingItem("Spanx" , 21.99, 4)
skirt = ShoppingItem("Skirt" , 10.50, 1)
crop = ShoppingItem("Crop Top", 16.99, 2)
hat = ShoppingItem("Cute Hat", 25.50, 2)

clothes_menu = { "1." : "-_-BACK-_-",
                 "2." : tennis_shoe.__rper__(),
                 "3." : spanx.__rper__(),
                 "4." : skirt.__rper__(),
                 "5." : crop.__rper__(),
                 "6." : hat.__rper__()
              }

#pattern after this would be class variables/menu for remaining sub menus. 
                
                

if __name__ == '__main__':
    #testing print_menus function
    print_menus(main_menu)
    print_menus(clothes_menu)

    #add_to_cart test; in actual version will have to update unit amount in both classes
    buy_cart.add_to_cart(tennis_shoe)
    buy_cart.add_to_cart(spanx)

    #how to print cart; def as a function in more developed version
    show_cart()

    #testing buy_cart; not complete yet, price does not reflect the spanx
    buy_cart.check_out()

    """
    how to target items in buy_cart
    print(buy_cart.cart[0].name)
    print(buy_cart.cart[0].price)
    print(buy_cart.cart[0].units)
    """
    


"""
This part down here isn't complete at all; skeleton in progress to try and help make sure my process is quasi logical

classes
functions
variables
dicts

increment = 0
while increment < 1:

        if __name__ == '__main__':
            print(Greetings!)
            print_menus(main_menu)
            #remember to strip input variables in future
            toggle_menu = input("Where would you like to browse? Have user select a-f; strip input of everything except letter and make it lowercase")

            if toggle_menu = a:
                #can turn this into one uniform function for all contingencies
                print_menus(clothes_menu) #replace clothes menu a variable for general function
                toggle_item = ("Which item would you like to purchase? Enter associated numeral")
                item_amount = input("How many units?")
                
                if item_amount > .units: #not sure if I will be able to acomplish this
"""
