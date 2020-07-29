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