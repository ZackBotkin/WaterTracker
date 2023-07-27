from water_tracker.src.io.query_runner import QueryRunner


class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def record_water(self, count):
        self.query_runner.insert_water(count)

    def get_waters(self):
        waters = self.query_runner.get_waters()
        return waters
