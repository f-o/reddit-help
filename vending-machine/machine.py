import json

# Load the inventory from the json file
with open('inventory.json') as f:
    inventory = json.load(f)


def main():
    while True:
        # Clear the screen
        print(chr(27) + "[2J")
        # Print the menu
        print("Welcome to the Vending Machine")
        for i, item in enumerate(inventory): # enumerate() returns a tuple of the index and the item so we can use it to get the index in the loop
            print(f'{i+1:02d}: {item["label"]}') # The index is 0 based so we add 1 to it to make it 1 based. We also pad it with a 0 so it's always 2 digits long.
        
        # Get the user's choice
        choice = int(input('Please select an item: ')) - 1 # We subtract 1 from the choice to get the index of the item in the list
        print(f'You selected {inventory[choice]["label"]}. That will be ${inventory[choice]["price"]}')
        
        # Get the user's payment
        change = float(input('Please insert money: '))
        if change < inventory[choice]['price']:
            print('You did not insert enough money')
            return
        
        # Update the inventory
        inventory[choice]['quantity'] -= 1
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f, indent=4)

        # Give the user their change
        print(f'Here is your {inventory[choice]["label"]} and ${change - inventory[choice]["price"]} in change')
        
        # Ask the user if they want to buy another item
        if input('Would you like to buy another item? (y/n) ') == 'n':
            print('Thank you for using the vending machine')
            break


if __name__ == '__main__':
    main()