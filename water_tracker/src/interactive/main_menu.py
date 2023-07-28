from datetime import datetime, timedelta
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

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            ReadTodaysWatersMenu(manager, self.path),
            ReadYesterdaysWatersMenu(manager, self.path)
        ]

    def title(self):
        return "Read"

class ReadTodaysWatersMenu(InteractiveMenu):

    def title(self):
        return "Today"

    def main_loop(self):
        date = datetime.now().strftime("%Y-%m-%d")
        print("")
        print(date)
        print("")
        count = self.manager.get_waters_count(date)
        print("\t> %d glasses of water consumed!" % count)
        print("")

class ReadYesterdaysWatersMenu(InteractiveMenu):

    def title(self):
        return "Yesterday"

    def main_loop(self):
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        print("")
        print(date)
        print("")
        count = self.manager.get_waters_count(date)
        print("\t> %d glasses of water consumed!" % count)
        print("")
