import random
from door import Door

class BasicDoor(Door):
    """Push-or-pull door.

    Randomly chooses the correct action (push or pull). You guess; the game tells
    you if it opened or nudges you to try the other way.
    """
    def __init__(self):
        """Set a hidden correct action (push or pull) and start closed."""
        self._correct = random.choice([1, 2])  # 1=Push, 2=Pull
        self._opened = False

    def examine_door(self):
        """Explain it’s a plain door you must either push or pull."""
        return "You encounter a basic door, you can either push it or pull it to open."

    def menu_options(self):
        """Return the two choices to show: 1) Push, 2) Pull."""
        return "1. Push\n2. Pull"

    def get_menu_max(self):
        """Report that the valid menu range is 1–2."""
        return 2

    def attempt(self, option):
        """Try the chosen action once and record whether it opened."""
        tried = "You push the door." if option == 1 else "You pull the door."
        self._opened = (option == self._correct)
        return tried

    def is_unlocked(self):
        """Tell whether the door is currently open."""
        return self._opened

    def clue(self):
        """Give a gentle nudge to try the other option."""
        return "Try the other way."

    def success(self):
        """Return the win message for opening the door."""
        return "Congratulations, you opened the door."
