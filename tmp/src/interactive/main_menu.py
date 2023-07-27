
from interactive_menu.src.interactive_menu import InteractiveMenu


class MainMenu(InteractiveMenu):

    def __init__(self, manager, paths=[]):
        super().__init__(manager, paths)
        self.sub_menu_modules = []

    def title(self):
        return "Main"
