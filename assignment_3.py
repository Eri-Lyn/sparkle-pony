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

   6. The items should all be apart of a new class called ShoppingItem. It should have the member variables:
      name, price, stock

If you have any questions let me know, as this is more involved. But, it uses all the stuff you've learned thus far,
like making a class and retrieving it from a list. And lots of printing and formatting. :^)
"""

