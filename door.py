from abc import ABC, abstractmethod

class Door(ABC):
    """Interface for all door types in the Escape Room game.
    Subclasses must implement every abstract method below.
    """

    @abstractmethod
    def examine_door(self):
        """Describe this door in a single sentence."""
        pass

    @abstractmethod
    def menu_options(self):
        """Return the input prompt or a numbered menu string to show the player."""
        pass

    @abstractmethod
    def get_menu_max(self):
        """Return the highest valid menu choice number for this door."""
        pass

    @abstractmethod
    def attempt(self, option):
        """Apply the player’s choice once and return a short past-tense description."""
        pass

    @abstractmethod
    def is_unlocked(self):
        """Return True when the door’s success condition is met; otherwise False."""
        pass

    @abstractmethod
    def clue(self):
        """Return a brief hint if the door is still locked after an attempt."""
        pass

    @abstractmethod
    def success(self):
        """Return the one-line success message shown when the door unlocks."""
        pass