import random
from door import Door

class LockedDoor(Door):
    """Key-hunt door.

    The key is hidden in one of three places (mat, flower pot, fake rock). Pick
    a spot each turn until you find it.
    """
    def __init__(self):
        """Hide the key in a random spot and start the door locked."""
        self._key_loc = random.choice([1, 2, 3])
        self._opened = False

    def examine_door(self):
        """Say the key is nearby and you’ll need to find it to open the door."""
        return "A locked door. The key is hidden nearby. Look around for the key."

    def menu_options(self):
        """Return the three search choices: doormat, flower pot, or fake rock."""
        return (
            "1. Look under the mat.\n"
            "2. Look under the flower pot.\n"
            "3. Look under the fake rock."
        )

    def get_menu_max(self):
        """Report that the valid menu range is 1–3."""
        return 3

    def attempt(self, option):
        """Search the chosen spot once and record if you found the key."""
        places = {
            1: "You look under the mat.",
            2: "You look under the flower pot.",
            3: "You look under the fake rock.",
        }
        self._opened = (option == self._key_loc)
        return places[option]

    def is_unlocked(self):
        """Tell whether the key was found and the door is unlocked."""
        return self._opened

    def clue(self):
        """Give a short nudge to try a different hiding place."""
        return "Look somewhere else."

    def success(self):
        """Return the win message for finding the key and opening the door."""
        return "You found the key and unlocked the door."
