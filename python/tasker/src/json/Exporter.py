import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks: list[dict]) -> None:
        with open("./taski.json", "w", encoding="utf8") as f:
            json.dump(tasks, f, ensure_ascii=False)
