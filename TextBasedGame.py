# Christopher Sawyer IT140 -- Text Based Game

def main():
    # Get debugmode to work within main function.
    global debugmode

    # Define the game rooms and items
    rooms = {
        'Foyer': {'East': 'Day Room',
                  'West': 'Lounge',
                  'Item': None,
                  'Desc': 'You see a bright room and entrance to the grand house.'},
        'Day Room': {'North': 'Great Hall',
                     'West': 'Foyer',
                     'Item': 'Gloves',
                     'Desc': 'Here is a relaxing sun-lit room for entertaining.'},
        'Lounge': {'North': 'Library',
                   'East': 'Foyer',
                   'Item': 'Pipe Fittings',
                   'Desc': 'You see a comfortable room for relaxing.'},
        'Great Hall': {'North': 'Parlor',
                       'South': 'Day Room',
                       'West': 'Library',
                       'Item': 'Hacksaw',
                       'Desc': 'You see a grand artery of the home, with large windows.'},
        'Library': {'North': 'Bedroom',
                    'South': 'Lounge',
                    'East': 'Great Hall',
                    'Item': 'Goggles',
                    'Desc': 'You enter a comfy space with books and comfortable seating.'},
        'Bedroom': {'South': 'Library',
                    'East': 'Bathroom',
                    'Item': 'Thread Sealant',
                    'Desc': 'You see a smaller room with a medium sized bed and wood furniture.'},
        'Bathroom': {'North': 'Master Bedroom',
                     'East': 'Parlor',
                     'West': 'Bedroom',
                     'Item': 'Pipe Wrench',
                     'Desc': 'You see a wonderfully designed relief area.'},
        'Parlor': {'North': 'Dining Room',
                   'South': 'Great Hall',
                   'West': 'Bathroom',
                   'Item': 'Copper Pipes',
                   'Desc': 'You see a welcoming room for chatting with guests.'},
        'Master Bedroom': {'South': 'Bathroom',
                           'Item': 'Adjustable Wrench',
                           'Desc': 'You see a large comfortable bed, and beautiful furniture.'},
        'Dining Room': {'South': 'Parlor',
                        'East': 'Kitchen',
                        'Item': 'Snake Machine',
                        'Desc': 'Delicious food is laid out on the table, laid out for many guests.'},
        'Kitchen': {'North': 'Basement',
                    'West': 'Dining Room',
                    'Item': 'Lunch',
                    'Desc': 'You smell delicious cooking from the stove, and vegetables on the counter.'},
        'Basement': {'Item': None,
                     'Desc': 'You see three feet of water and a huge waterfall-like leak!'}
    }

    show_instructions()  # Show the game intro

    # Initialize the location and the inventory
    current_location = 'Foyer'
    inventory = []

    # The main game loop, continues while the current
    # location is not the basement
    while current_location != 'Basement':

        # Show the main game user interface
        print('\n')
        player_status(current_location, inventory, rooms)
        action, article = process_input(input('Enter your move: '))
        print()
        debugmessage(f'Entered: {action}, {article}')

        # Validate the action command and call the appropriate functions
        if action == 'Go' or action == 'Move':
            # Update the current location with the function
            current_location = move_location(article, current_location, rooms)
        elif action == 'Get':
            # Update the inventory with the function
            inventory = item_get(article, rooms[current_location]['Item'], inventory)
        elif action == 'Activate' and article == 'Godmode':
            # Turn on debug mode, give all items by typing 'activate godmode'
            if debugmode is False:
                for room in rooms:
                    inventory = item_get(rooms[room]['Item'], rooms[room]['Item'], inventory)
                    debugmode = True
            else:
                debugmessage('Debug mode is already activated.')
        elif action == 'Teleport' and debugmode is True:  # Teleport command enabled only when debug mode is on
            current_location = article if article in rooms else current_location
        else:
            print('Cannot understand command. Please try again.')

    # The end of the loop assumes that the current location is the basement
    if len(inventory) == 10:  # If player has 10 items, they've collected enough to win
        print('\n')
        print('*' * 80)
        print(rooms[current_location]['Desc'])
        print('Luckily, you\'ve collected all of your tools!')
        print('You quickly and deftly turn off the water main, cut the broken sections out,')
        print('and replace the pipes. The customer is glad and leaves you a positive Yelp')
        print('review! Congratulations! The Super Luigi Bros. Plumbing Company is')
        print('a 5-star company!')
        print('                                   THE END')
        print('*' * 80)
        input('Press any key to quit.')
    else:
        print('\n')
        print('*' * 80)
        print(rooms[current_location]['Desc'])
        print('Unfortunately, you don\' have all of your tools.')
        print('You try to replace the broken section of pipe, but forgot to turn off the')
        print('water main. You dont have enough to properly seal the pipes or stop the leak.')
        print('The customer is mad, and leaves you a bad Yelp review!')
        print('The Super Luigi Bros. Plumbing company is a 1-star company. Too bad.')
        print('                                   THE END')
        print('*' * 80)
        input('Press any key to quit.')


def debugmessage(message):
    # This function only prints debug messages if the global variable is true.
    if debugmode is True:
        print(message)


def move_location(direction, location, rooms):
    # Check if the direction is in the room's dictionary
    if direction in rooms[location]:
        new_room = rooms[location][direction]
        print(f'*** You walk {direction}. ***')
    else:
        new_room = location  # Set the new room location to the original
        print('Nothing in that direction.')
    return new_room


def item_get(user_term, room_item, inventory):
    # Check if the user's term exists as a valid item
    if user_term != room_item:
        print(f'Cannot get the {user_term}!')
    # Check if the user's term exists in the user's inventory
    elif user_term in inventory:
        print(f'You already have the {user_term}!')
    # Edge case if user enters nothing
    elif user_term is None:
        pass
    else:  # Else, add the item to the player's inventory
        print(f'*** You got the {room_item}! ***')
        inventory.append(room_item)
    return inventory


def show_instructions():
    print('*' * 80)
    print('                   Welcome to "Super Luigi Bros"!')
    print('You are a plumber for the Super Luigi Bros. Plumbing company and have just')
    print('been called to a job at a maze of a house! There is flooding and a terrible')
    print('leak in the basement. Your apprentice delivered all of your tools to the')
    print('home, but accidentally dropped them in various rooms of the house.')
    print('Collect all your tools before tackling the job!')
    print()
    print('Enter a command to explore the house and pick up your items.')
    print('You can type "go North" or "get Pipe fittings" for example.')
    print('*' * 80)
    input('Press enter to continue.')
    print('\n\n')


def player_status(location, inventory, rooms):
    print('-' * 80)
    print(f'You are in the {location}.')
    print(rooms[location]['Desc'])
    item = rooms[location]['Item']
    if (item not in inventory) and (item is not None):
        print(f'You can see a {item} in the room.')
    print(f'Inventory: {inventory}')
    print('-' * 80)


def process_input(usr_input):
    # Process the input and make sure it is formatted correctly
    usr_input = usr_input.lower().split()

    # Make sure the user actually entered at least two terms
    # If not, set to blank list
    if len(usr_input) < 2:
        usr_input = ['', '']

    # Capitalize each term
    for index, term in enumerate(usr_input):
        usr_input[index] = term.capitalize()

    # Join room names or item names together into one string
    # ex. 'Great' 'Hall' -> 'Great Hall'
    # Then strip leading and following whitespace
    if len(usr_input) > 2:
        new_element = ''
        for index, term in enumerate(usr_input):
            if index > 0:
                new_element += f'{term} '
        usr_input = [usr_input[0], new_element.strip()]
    return usr_input[0], usr_input[1]


if __name__ == '__main__':
    debugmode = False
    main()
