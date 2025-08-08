import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.convert_json_to_dict()

    def convert_json_to_dict(self):
        with open(self.file_path) as file:
            return json.load(file)

