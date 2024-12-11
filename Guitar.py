from abc import ABC, abstractmethod

class Guitar(ABC):
    def __init__(self, model_name, number_of_strings, manufacturer):
        self.model_name = model_name
        self.number_of_strings = number_of_strings
        self.manufacturer = manufacturer

    @abstractmethod


    def get_info(self, db_manager):
        sql = "SELECT model_name, number_of_strings, manufacturer FROM guitars WHERE model_name = %s"
        db_manager.cursor.execute(sql, (self.model_name,))
        result = db_manager.cursor.fetchone()
        if result:
            model_name, number_of_strings, manufacturer = result
            return f"Model: {model_name}, Strings: {number_of_strings}, Manufacturer: {manufacturer}"
        else:
            return f"Gitara {self.model_name} nie istnieje w bazie."
