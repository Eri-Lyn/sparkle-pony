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

"""
SUMMARY
``````````````````````````````````````````````````````````````````````````````````
- I notice your new methods on making things modular, however none of them seem to be usable. :')
  I wouldn't make a method for something unless you'll be using it a lot.
- Change up your docstrings - or, the explanations of your functions. Put them in triple quotes directly
  under your function, and if there are any arguments, explain their purpose.
- You will almost never use constants/global variables unless they are for future proofing or math readability.
  Ex: PI = 3.14159, SERVER_PORT = 45589
- Try to make your variables readable. If another programmer has to investigate a variable's use for longer than
  30 seconds, something is probably wrong.
- Use the KISS method: Keep It Simple Stupid. Your functions should have one major purpose with expected inputs
  and outputs, and those inputs/outputs should be clarified in their docstring.
  Ex: sum(x, y) should say 'RETURNS the sum of two floats x and y.' It shouldn't do anything else. That way if a 
  user accidentally submits strings, or expects an integer back, that's their problem - not yours.
"""

#Between animalList and animal_list - which is prefered way to write a variable? Personal preference?
''' 
For variables we use camelCase. That is, start lower case and then every word is capitalized with
no spaces. thisIsAnExample. hereIsAnotherOne. 
For functions/methods we do all lower case with underscores. this_is_an_example_function.
For constants we do ALL_CAPS. EXAMPLE_CONSTANT. SERVER_NAME.
'''

#creating class animal; def __init_ is a constructor; arguments = class variables; first variable refernces object
''' 
I love your eager amount of comments. Programmers who don't comment are devils. However, commenting the basics
of python classes is a little redunant. Unless this is just for yourself. :V
'''
from operator import attrgetter

# camelCase for classes, except all are capitalized.
# Ex: Animal. TestClass. NewClassForEri. AnotherExampleClass
class animal:
    
    def __init__( self, name, color, sound, type):
        # As simple as this looks, this is usually how __init__ looks. Nice job!
        self.name = name
        self.color = color
        self.sound = sound
        self.type = type
    
    #formatting for presenting whole list of animal      <- nitpicky, but remove all whitespace after lines like this
    def __repr__(self):
        # Cheater!
        return 'The {0} {1} goes \'{2}!\'\n' .format(self.color, self.name, self.sound)
    
    #formatting for what animal user will select
    def __getitem__(self, name):
        return '---> {0}' .format(self.name)

#creating global variables; filling the barn via a list.
'''
Global variables/Constants are almost NEVER a good idea unless it's something you'll be changing in the future.
These should have been declared in the __main__ at the bottom, or a method should have been made to set these up.

A common example is if your script connects to some website. The constant would be:
DOMAIN_URL = www.fakedomain.com
If that ever changes in the future, you can just change that one constant so that you don't have to go through
and edit the whole damn script.
'''
cow = animal("cow", "brown", "Moo", "Mammal")
cat = animal("cat", "white", "Mew", "Mammal")
dog = animal("dog", "black", "Bark", "Mammal")
liz = animal("lizard", "green", "UwU", "Reptile")
rat = animal("rat", "grey", "Squeak", "Mammal")
horse = animal("horse", "tan", "Neigh", "Mammal")

'''
I didn't expect it, but I would have given bonus points if you assigned the animal colors and type to an Enum. :)
'''

barn_list = [cow, cat, dog, liz, rat, horse]

#1st function: welcome user; print names of animals; and allow them to itterate one.
#global variable most likely improper, but easiest way I could find to attach variable to next function
def present_barn():
    print ("Welcome to the barn!\nFor animals we have a:\n")
    
    for instance in barn_list:  
        print(instance[0].title())

    # Always try and make your variables readable. Any new programmer who would see this hypothetical script in
    # the future would have no idea what x or y are. barnIter or animNum are options.
    global x
    y = None  # This could be set as a Boolean instead. Only options are True/False for booleans.
              # Likewise, could be named 'validOption'.
    while y is None:
        x = input("Iterate them for more details using a single numeral between 0 and 5:")
        if x.isdigit():
            x = int(x)
            if x >= 0 and x <= 5:
                x = int(x)  # Why are you doing this twice?
                y = 1
            else:
               print("Please enter a numeric value between 0 and 5.")
        else:
            print("Please enter a numeric value between 0 and 5 using digits only.")
    return x
 
#function takes return value from present_barn and displays it in repr form
'''
When doing a 'doc string' - AKA, an explanation of a method - put it directly under the method in triple quotes.
Also, if anyone else were to use this function, they wouldn't know what you're talking about. You have to either
include this method in the animal class, or give it a more abstract explanation.
'''
def list_animal(x):
    """ Takes return value from present_barn and displays it in repr form

    x -- The index in the barn_list
    """
    print("")  # You could just put '\n' at the beginning of the next print.
    print (barn_list[x])  # Be careful of little white space issues, like the space after print
    print("Afraid you missed out on some of your furry friends? Here's the whole list!\n")
    print('\n' , *barn_list, sep="")
# I see you're trying to make the script modular - which is great! - however this method seems to defeat the purpose.
# Instead of just printing out what the user wants - which you don't need a method for that one line - you also
# print out all the animals in the list which seems counter productive.

#function sorts list and shows repr format for sorted animals    
def sort(barn_list):
    input("Now we will sort our friends alphabetically by color~\nEnter any value to continue:")
    # You ask for an unknown value then never use it. :')
    sorted_barn_list = sorted(barn_list, key=attrgetter('color'))  # Nice!
    print('\n' , *sorted_barn_list, sep="")

#purpose of if name = main syntax is to prevent confusion when incorportating outside files?
''' 
This block of code is the starting point. It's like int main() in C++ if you know what I'm talking about.
Regardless, this is the root of all your calls. It makes it easy to organize your thoughts, methods, and
can also make testing easier in the future. Like, comment out one method or throw temp variables in here.
'''
#asserts above funtions
if __name__ == '__main__':
    
    present_barn()  # present_barn() is returning a variable, but you haven't assigned it to anything.
                    # You probably meant to put something like:
                    #   var = present_barn()
    list_animal(x)  # Read above
    sort(barn_list)
