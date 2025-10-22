import random
from door import Door

class CodeDoor(Door):
    """Three-character X/O toggle lock.

    The solution is a secret pattern of X and O. Pressing key 1–3 flips that
    position between X and O. Open when your row matches the solution.
    """
    def __init__(self):
        """Pick a secret X/O pattern and start with a fresh, closed lock."""
        self._solution = [random.choice(['X', 'O']) for _ in range(3)]
        self._current = ['X', 'X', 'X']
        self._opened = (self._current == self._solution)

    def examine_door(self):
        """Explain that pressing 1–3 flips that position between X and O."""
        return ("A door with a coded keypad with three characters. "
                "Each key toggles a value with an 'X' or an 'O'.")

    def menu_options(self):
        """Return numbered key options."""
        return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3"

    def get_menu_max(self):
        """Report that the valid menu range is 1–3."""
        return 3

    def attempt(self, option):
        """Flip the chosen position and record whether the pattern now matches."""
        idx = option - 1
        self._current[idx] = 'O' if self._current[idx] == 'X' else 'X'
        self._opened = (self._current == self._solution)
        return f"You press key {option}."

    def is_unlocked(self):
        """Tell whether the current X/O row matches the secret code."""
        return self._opened

    def clue(self):
        """Give a quick hint about which positions are currently correct."""
        names = ["first", "second", "third"]
        correct_positions = [i for i in range(3) if self._current[i] == self._solution[i]]
        if len(correct_positions) == 0:
            return "None of the characters are correct."
        if len(correct_positions) == 3:
            return "All three characters are correct."
        if len(correct_positions) == 1:
            return f"Only the {names[correct_positions[0]]} character is correct."
        pair = " and ".join(names[i] for i in correct_positions)
        return f"The {pair} characters are correct."

    def success(self):
        """Return the win message for entering the correct code."""
        return "You entered the correct code and opened the door."