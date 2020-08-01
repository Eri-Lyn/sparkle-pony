"""
ASSIGNMENT 1 -- INTRO
````````````````````````````````````````````````````````````````````````````````````````
1. Print out a greeting to the user
2. Make a function that adds two variables together and prints the output
3. Break a given string into a character array, then print the letters in alphabetical order with no duplicates.
   In python, an 'array' is generally a list.
"""


letters = []

print("Hello there! Let's add some numbers.")

while True:
    try:
       var1 = float(input("Enter an integer:"))
       vsum = str((var1 + float(input("And another:"))))
       break
    except ValueError:
       print("Whoops!")

print("The sum is:" , vsum)

while True:
    word = str(input("Enter a word:"))
    if word.isdigit():
        print("No integers or floats, please.")
    else:
        break
        
for  letter in word:
    if letter in letters:
        pass
    else:
        letters.append(letter)
   
print(letters)