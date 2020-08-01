# -*- coding: utf-8 -*-
"""
ASSIGNMENT 2 -- CLASSES
````````````````````````````````````````````````````````````````````````````````````````
1. Create a class called 'Animal'. It should have the following member variables:
   name  (ex. Cow)
   color (ex. Brown)
   sound (ex. Moo)
   type  (ex. Mammal)

2. Make a LIST of this Animal type. This list should be iterable and callable. In other words, if you return
   animalList[2], it should neatly output those member variables in some fashion. Likewise, you need a way
   to sort this class (which I will leave up to you). Attempting to call sort(animalList) should return a list
   of Animal objects organized by X member variable.

"""
#Between animalList and animal_list - which is prefered way to write a variable? Personal preference? 

#creating class animal; def __init_ is a constructor; arguments = class variables; first variable refernces object
from operator import attrgetter

class animal:
    
    def __init__( self, name, color, sound, type):
        self.name = name
        self.color = color
        self.sound = sound
        self.type = type
    
    #formatting for presenting whole list of animal   
    def __repr__(self):
        return 'The {0} {1} goes \'{2}!\'\n' .format(self.color, self.name, self.sound)
    
    #formatting for what animal user will select
    def __getitem__(self, name):
        return '---> {0}' .format(self.name)

#creating global variables; filling the barn via a list.
cow = animal("cow", "brown", "Moo", "Mammal")
cat = animal("cat", "white", "Mew", "Mammal")
dog = animal("dog", "black", "Bark", "Mammal")
liz = animal("lizard", "green", "UwU", "Reptile")
rat = animal("rat", "grey", "Squeak", "Mammal")
horse = animal("horse", "tan", "Neigh", "Mammal")

barn_list = [cow, cat, dog, liz, rat, horse]

#1st function: welcome user; print names of animals; and allow them to itterate one.
#global variable most likely improper, but easiest way I could find to attach variable to next function
def present_barn():
    print ("Welcome to the barn!\nFor animals we have a:\n")
    
    for instance in barn_list:  
        print(instance[0].title())
        
    global x
    y = None
    while y is None:
        x = input("Iterate them for more details using a single numeral between 0 and 5:")
        if x.isdigit():
            x = int(x)
            if x >= 0 and x <= 5:
                x = int(x)
                y = 1
            else:
               print("Please enter a numeric value between 0 and 5.")
        else:
            print("Please enter a numeric value between 0 and 5 using digits only.")
    return x
 
#function takes return value from present_barn and displays it in repr form
def list_animal(x):
    print("")
    print (barn_list[x])
    print("Afraid you missed out on some of your furry friends? Here's the whole list!\n")
    print('\n' , *barn_list, sep="")

#function sorts list and shows repr format for sorted animals    
def sort(barn_list):
    input("Now we will sort our friends alphabetically by color~\nEnter any value to continue:")
    sorted_barn_list = sorted(barn_list, key=attrgetter('color'))
    print('\n' , *sorted_barn_list, sep="")

#purpose of if name = main syntax is to prevent confusion when incorportating outside files?
#asserts above funtions
if __name__ == '__main__':
    
    present_barn()
    list_animal(x)
    sort(barn_list)
    

