import random
from door import Door

class ComboDoor(Door):
    """Spin-the-dial door.

    There’s a hidden number from 1–10. You enter guesses; the game tells you
    “Too high.” or “Too low.” until you land on the exact value.
    """
    def __init__(self):
        """Pick a secret number from 1–10 and start the door locked."""
        self._solution = random.randint(1, 10)
        self._last_val = 0
        self._opened = False

    def examine_door(self):
        """Explain it’s a 1–10 combo lock and you enter one number per try."""
        return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

    def menu_options(self):
        """Return the single prompt string asking for a number from 1–10."""
        return "Enter a number (1-10): "

    def get_menu_max(self):
        """Report that the maximum valid input is 10."""
        return 10

    def attempt(self, option):
        """Record the guess and check it against the secret number."""
        self._last_val = option
        self._opened = (option == self._solution)
        return f"You turn the dial to... {option}"

    def is_unlocked(self):
        """Tell whether the last guess equals the secret number."""
        return self._opened

    def clue(self):
        """Give a quick ‘Too high.’ or ‘Too low.’ hint after a wrong guess."""
        return "Too high." if self._last_val > self._solution else "Too low."

    def success(self):
        """Return the win message for dialing the correct number."""
        return "You found the correct value and opened the door."
