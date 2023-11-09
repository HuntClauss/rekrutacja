import json


class Importer:
    __slots__ = ["tasks"]

    def __init__(self):
        self.tasks: list[dict] = []
        pass

    def read_tasks(self) -> None:
        with open("./taski.json", "r", encoding="utf8") as f:
            self.tasks = json.load(f)

    def get_tasks(self) -> list[dict]:
        return self.tasks
