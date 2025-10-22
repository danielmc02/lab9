import random
from door import Door

class DeadboltDoor(Door):
    """Double-bolt mystery.

    Two deadbolts must both be unlocked, but you can’t tell their states by sight.
    Each turn you toggle bolt 1 or bolt 2 and feel for progress.
    """
    def __init__(self):
        """Start with two bolts in random states and the door locked."""
        self._bolt1_locked = bool(random.getrandbits(1))
        self._bolt2_locked = bool(random.getrandbits(1))
        self._opened = (not self._bolt1_locked) and (not self._bolt2_locked)

    def examine_door(self):
        """Say there are two bolts and you can only toggle them."""
        return ("You encounter a double deadbolt door, both deadbolts must be "
                "unlocked to open it, but you can't tell from looking at them "
                "whether they’re locked or unlocked.")

    def menu_options(self):
        """Return the two choices: toggle bolt 1 or toggle bolt 2."""
        return "1. Toggle Bolt 1\n2. Toggle Bolt 2"

    def get_menu_max(self):
        """Report that the valid menu range is 1–2."""
        return 2

    def attempt(self, option):
        """Toggle the chosen bolt and record whether both bolts are now unlocked."""
        if option == 1:
            self._bolt1_locked = not self._bolt1_locked
            tried = "You toggle the first bolt."
        else:
            self._bolt2_locked = not self._bolt2_locked
            tried = "You toggle the second bolt."
        self._opened = (not self._bolt1_locked) and (not self._bolt2_locked)
        return tried

    def is_unlocked(self):
        """Return True if both bolts are unlocked."""
        return self._opened

    def clue(self):
        """Return clue: either 'one bolt is unlocked' or 'completely locked'."""
        one_unlocked = (not self._bolt1_locked) ^ (not self._bolt2_locked)
        if one_unlocked:
            return "You jiggle the door... it seems like one of the bolts is unlocked."
        return "You jiggle the door... it’s completely locked."

    def success(self):
        """Return the win message for freeing both bolts."""
        return "You unlocked both deadbolts and opened the door."