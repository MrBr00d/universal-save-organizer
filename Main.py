import os
import shutil
import pickle
from pathlib import Path



"""Need to check about the save location. This should all be \\ not sure how tkinter handles this"""
# def save_dict():
#     """Function that serializes all games"""
#     with open("Organizer.Game_dict.pkl", 'wb') as f:
#         pickle.dump(Organizer.Game_dict, f)

# def load_dict():
#     """Function that loads in previously added games"""
#     with open('Organizer.Game_dict.pkl', 'rb') as f:
#         Organizer.Game_dict = pickle.load(f)

class Game:
    def __init__(self, name, save_location):
        """Game class containing all game and savefile information.
        name: (str) name of the game.
        save_location: (str) path of the savefile location"""
        self.name = name
        self.save_location = Path(save_location)
        self.directory = self.save_location.parent
        self.profiles = [item.name for item in os.scandir(self.directory) if item.is_dir()]
        self.save_extention = self.save_location.suffix

    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.directory
    
    def get_profiles(self):
        return self.profiles
    
    def set_location(self, save_location):
        self.save_location = Path(save_location)
        self.directory = self.save_location.parent
        self.profiles = [item.name for item in os.scandir(self.directory) if item.is_dir()]
        Organizer.save_dict()
    
    #Profile management functions 
    def create_profile(self, profile_name):
        Path(self.directory, profile_name).mkdir()
        print("Profile added.")

    def remove_profile(self, profile_name):
        shutil.rmtree(os.path.join(self.directory, profile_name))

    def show_profile(self):
        return [item.name for item in os.scandir(self.directory) if item.is_dir()]
    
    def get_sections(self, profile_name):
        return[item.name for item in os.scandir(os.path.join(self.directory, profile_name)) if item.is_dir()]
    
    def import_save(self, profile, section):
        """Imports the save to a profile and section. Profile can be any% for instance and section the part of the run to be saved.
        profile: (str) e.g. any%/all bosses.
        section: (str) e.g. intro/first bossfight/final boss"""
        save_target = os.path.join(self.directory, profile, section, self.save_location.name)
        save_dir = os.path.join(self.directory, profile, section)
        if os.path.isdir(f"{self.directory}\\{profile}"):
            os.makedirs(save_dir, exist_ok=True)
            shutil.copyfile(self.save_location, save_target)
        else:
            print("Profile not found.")

    def load_save(self, profile, section):
        save_target = os.path.join(self.directory, profile, section, self.save_location.name)
        shutil.copy(save_target, self.directory)

class Organizer:
    Game_dict: dict[str, Game] = {}
    def __init__(self):
        """Upon starting the program the games are loaded if the file exists"""
        if "Organizer.Game_dict.pkl" in os.listdir():
            Organizer.load_dict()
            print("Organizer.Game_dict loaded.")
    
    @staticmethod
    def add_game(name, save_location):
        """Function to add a game and create a game instance. This instance is then saved in the Organizer.Game_dict dictionary and saved.
        name: (str) name of the game.
        save_location: (str) location of the savefile."""
        if name not in Organizer.Game_dict.keys():
            Organizer.Game_dict[name] = Game(name, save_location)
            Organizer.save_dict()
            print("Game added.")
        else:
            print("Game already in game list.")
    @staticmethod
    def remove_game(name):
        """Remove game from dictionary and saves to file.
        name: (str) name of the game to be removed"""
        if name in Organizer.Game_dict.keys():
            Organizer.Game_dict.pop(name)
            Organizer.save_dict()
            print("Game removed.")
        else:
            print("Game not found.")

    @staticmethod
    def get_games():
        """Lists all games in the Games_dict file"""
        return list(Organizer.Game_dict.keys())
    
    @staticmethod
    def load_dict():
        """Function that loads in previously added games"""
        with open('Organizer.Game_dict.pkl', 'rb') as f:
            Organizer.Game_dict = pickle.load(f)
    
    @staticmethod
    def save_dict():
        """Function that serializes all games"""
        with open("Organizer.Game_dict.pkl", 'wb') as f:
            pickle.dump(Organizer.Game_dict, f)
