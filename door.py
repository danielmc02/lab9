from abc import ABC, abstractmethod

class Door(ABC):
    
    @abstractmethod
    def examine_door(self): # returns a string description of the door
        pass
    
    @abstractmethod
    def menu_options(self): # returns a string of the menu options that user can choose from when attempting to unlock the door.
        pass
    
    @abstractmethod
    def get_menu_max(self): # returns the number of options in the above menu
        pass
    
    @abstractmethod
    def attempt(self,option): # returns a string description of the door
        pass
    
    @abstractmethod
    def is_unlocked(self): # checks to see if the door was unlocked, returns true if it is, false otherwise
        pass
    
    @abstractmethod
    def clue(self): # returns the hint that is returned if the user was unsuccessful at their attempt
        pass
    
    
    @abstractmethod
    def success(self): # returns the congratulatory message if the user was successful
        pass
    
    
    
    
class BasicDoor(Door):
    def __init__(self):
        self.
        
    def examine_door(self):
        
        return "A door that is either pushed to open, or pulled."
    
    def menu_options(self):
        return "1. Push\n2. Pull"
    
    def clue(self):
        return "Try the other way."
    
class LockedDoor(Door):
    def __init__(self):
        "Randomizes the location of the key."
    def examine_door(self):
        return "A locked door.The key is hidden nearby. Look around for the key."
    def menu_options(self):
        return "1. Look under the mat. 2. Look under the flower pot. 3. Look under the fake rock."