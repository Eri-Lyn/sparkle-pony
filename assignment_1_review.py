"""
ASSIGNMENT 1 -- INTRO
````````````````````````````````````````````````````````````````````````````````````````
1. Print out a greeting to the user
2. Make a function that adds two variables together and prints the output
3. Break a given string into a character array, then print the letters in alphabetical order with no duplicates.
   In python, an 'array' is generally a list.
"""

########################################################################################################################
######### ORIGINAL CODE ################################################################################################
########################################################################################################################

letters = []

print("Hello there! Let's add some numbers.")

while True:  # Be careful when doing this; it's usually better to put an actual condition to check instead of
   # having to break from a loop. But, it's not too big of a deal.
   try:
      var1 = float(input("Enter an integer:"))
      vsum = str((var1 + float(input("And another:"))))
      break
   except ValueError:  # Don't be TOO eager to try/except every block. Most of the time it's better to let the
      # interpret handle the error. All you're doing is saying "Whoops!" which tells the user
      # nothing about the actual error. Something you COULD do is re-write this to say:
      #
      # exception ValueError as e:
      #    print("Whoops! Error: {0}".format(e))
      print("Whoops!")

print("The sum is:", vsum)

while True:
   word = str(input("Enter a word:"))
   if word.isdigit():  # What happens if they put a special character?
      print("No integers or floats, please.")
   else:
      break

for letter in word:  # This is how I would do this if I didn't know about set() - which you can see down
   # below. Pretty straightforward, which is usually the best option!
   if letter in letters:
      pass
   else:
      letters.append(letter)

print(letters)


########################################################################################################################
########### NEW CODE ###################################################################################################
########################################################################################################################

# This is going to look obnoxious, as it over doubled the size of the program, but I want you to keep some things in
# mind when reading this:
#   1. How easy is this file to reference in other scripts?
#   2. Is there a way to future proof this?
#   3. Is this modular enough, and therefore simple to test?
#   4. Could I break this? If so, how?
#
# And also, START FROM THE VERY BOTTOM. That's where the main entry point is!


def add_two_numbers():
   """ Greets the user and prompts for two numbers, then returns their sum. """
   greeting('Howdy! Let\'s get to summing!')
   firstVar = get_float_input()
   secondVar = get_float_input()
   print('The sum is: {0}'.format(sum_vars(firstVar, secondVar)))
   # The above is a very handy and highly encouraged method of inserting variables into a string.
   # This automatically formats them into a string, no matter what is given. Adding more variables looks like this:
   #
   # print("{0} is bigger than {1} but less than {2}".format(5, three, IX))


def greeting(text):
   """ Greets the user with whatever message you like by formatting the header. """
   print('.-+*` {0} `*+-.'.format(text))
   print('___________________________________________________________')


def get_float_input():
   """ Prompts the user for input, and returns a confirmed float. """
   userVar = None
   while not userVar:
      userVar = input('Enter a number: ')
      if not userVar:
         print('Nothing given! Please try again.')
      if not userVar.isdigit():
         print('Numbers only, please!')

   return float(userVar)


def sum_vars(varA, varB):
   """ Sums together two variables as floats. """
   # Convert to float in case this function is called elsewhere
   return float(varA) + float(varB)


def string_breakdown():
   """ Takes a user-given string and breaks it into characters, printing them in alphabetical order. """

   # Prompt the user for a string
   strVar = get_string_input()

   # Breakdown thier string into a list of alphabetical characters
   breakdownList = break_down_string(strVar)

   # Print it neatly to the terminal
   print('Sorted characters: ')
   print_list(breakdownList)


def get_string_input():
   """ Prompts the user for input, and returns a confirmed string. """
   userVar = None
   while not userVar:
      userVar = input('Enter a string: ')
      if not userVar:
         print('Nothing given! Please try again.')
      if not userVar.isalpha():
         print('No numbers or special characters, please!')

   return userVar


def break_down_string(str):
   """ Returns a sorted list of each character in the given string with no duplicates. """
   # First we make a set from the given string by splitting it into all its characters. A SET is different from a list
   # by storing unorganized data, but it guarantees no duplicates.
   breakdownSet = set(str.split())

   # Convert your unorganized mess into a list (or array). sorted() is a built-in function that returns a sorted list
   # from what you give it.
   return sorted(breakdownSet)


def print_list(listVar):
   """ Prints a given list in a cleaner, comma-delimited output. """
   printString = ""
   # Iterate through every item to format into this string
   for item in listVar:
      printString += '{0}, '.format(item)

   # When finished, remove the last two characters (a comma and space) to make it neater
   printString = printString[:-2]
   print(printString)


if __name__ == '__main__':
   # It's good practice to make your code 'modular'. The best way to do this in python is to make this block of
   # code on the bottom, which acts as the starting point in your code. It HAS to be on the bottom so that it
   # has everything above it as reference. 'What will be above it?' you ask? All your methods!

   # First let's add two variables
   add_two_numbers()

   # Now let's break a string into non-repeating, alphabetical characters
   string_breakdown()
