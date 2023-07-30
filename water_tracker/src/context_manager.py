from water_tracker.src.io.query_runner import QueryRunner


class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def record_water(self, count, date=None):
        self.query_runner.insert_water(count, date)

    def get_waters(self, date=None):
        waters = self.query_runner.get_waters(date)
        return waters

    def get_waters_count(self, date=None):
        waters = self.query_runner.get_waters(date)
        count = 0
        for water in waters:
            count += water[1]
        return count
