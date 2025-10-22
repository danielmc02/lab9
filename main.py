"""
LAB #9
    10/22/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    Escape Room: Interface-based door puzzle with five door types.
    Unlock three randomly selected doors using menus and clues to escape.
"""
import random
import check_input
from basic_door import BasicDoor
from code_door import CodeDoor
from deadbolt_door import DeadboltDoor
from locked_door import LockedDoor
from combo_door import ComboDoor

def open_door(door):
    """Run one door puzzle: show description, prompt for a move, apply it, hint if needed, and loop until unlocked."""
    print(door.examine_door())
    while True:
        menu = door.menu_options()
        prompt = "" if "\n" in menu else menu
        if menu and "\n" in menu:
            print(menu)

        choice = check_input.get_int_range(prompt, 1, door.get_menu_max())
        print(door.attempt(choice))

        if door.is_unlocked():
            print(door.success())
            break
        else:
            print(door.clue())

def main():
    """Escape Room launcher.

    Welcomes the player, randomly picks three door types (with a fresh instance
    each time), and runs them back-to-back using `open_door`. Prints a final
    “you escaped” message when all three are unlocked.
    """
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...\n")

    door_types = [BasicDoor, CodeDoor, DeadboltDoor, LockedDoor, ComboDoor]

    for _ in range(3):
        DoorClass = random.choice(door_types)
        d = DoorClass()
        open_door(d)
        print()

    print("Congratulations! You escaped...this time.")

if __name__ == "__main__":
    main()
