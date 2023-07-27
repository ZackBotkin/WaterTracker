
from interactive_menu.src.interactive_menu import InteractiveMenu


class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            RecordWaterMenu(manager, self.path),
            ReadWaterMenu(manager, self.path)
        ]

    def title(self):
        return "Main"

class RecordWaterMenu(InteractiveMenu):

    def title(self):
        return "Record"

    def main_loop(self):
        print("How many glasses?")
        count = self.fancy_input()
        self.manager.record_water(count)

class ReadWaterMenu(InteractiveMenu):

    def title(self):
        return "Read"

    def main_loop(self):
        waters = self.manager.get_waters()
        for water in waters:
            print(water)
