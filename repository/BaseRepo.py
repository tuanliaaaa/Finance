import json
from finance.settings import BASE_DIR
import os
class BaseRepo:
    def __init__(self, file_path: str):
        self.file_path = os.path.join(BASE_DIR, 'entity',file_path+'.json')

    def _read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_file(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def find_by_key(self, key: str, value):
        data = self._read_file()
        result = [item for item in data if item.get(key) == value]
        return result
    def add(self, item: dict):
        data = self._read_file()
        data.append(item)
        self._write_file(data)

    def update(self, key: str, key_value, updates: dict):
        data = self._read_file()
        item_found = False

        for item in data:
            
            if item.get(key) == key_value:
                item_found = True
                item.update(updates)
                break

        if item_found:
            self._write_file(data)
        else:
            raise ValueError(f"Item with {key} = {key_value} not found.")

    def delete(self, key: str, key_value):
        data = self._read_file()
        new_data = [item for item in data if item.get(key) != key_value]

        if len(new_data) == len(data):
            raise ValueError(f"Item with {key} = {key_value} not found.")
        else:
            self._write_file(new_data)

