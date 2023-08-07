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

    def main_loop(self, **kwargs):

        if "continued_commands" in kwargs:
            continued_commands = kwargs["continued_commands"]
            if len(continued_commands) == 1:
                count = continued_commands.pop(0)
                date = datetime.now().strftime("%Y-%m-%d")
                self.manager.record_water(count, date)
            elif len(continued_commands) == 2:
                count = continued_commands.pop(0)
                date = continued_commands.pop(1)
                self.manager.record_water(count, date)
            else:
                print("TOO many arguments!!!")
                print("Aborting")
        else:
            form_results = self.interactive_form(
                [
                    {
                        "question": "How many glasses of water?",
                        "expected_response_type": "INT",
                        "return_as": "count",
                        "default": "",
                        "allow_empty": False
                    },
                    {
                        "question": "What date? (YYYY-MM-DD) Hit enter for today",
                        "expected_response_type": "YYYYMMDD_Date",
                        "return_as": "date",
                        "default": datetime.now().strftime("%Y-%m-%d"),
                        "allow_empty": False
                    }
                ]
            )
            if form_results["user_accept"] != True:
                print("Aborting!")
                return
            form_results.pop("user_accept")
            for answer_key in form_results.keys():
                if not form_results[answer_key]["valid"]:
                    print("%s is not a valid value! Aborting" % answer_key)
                    return

            count = form_results["count"]["value"]
            date = form_results["date"]["value"]
            self.manager.record_water(count, date)

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
