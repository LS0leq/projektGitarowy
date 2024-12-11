from Guitar import Guitar

class AcousticGuitar(Guitar):
    stringReplacementCost = 10

    def __init__(self, model_name, number_of_strings, manufacturer, wood_type, played_hours=0):
        super().__init__(model_name, number_of_strings, manufacturer)
        self.wood_type = wood_type
        self.played_hours = played_hours



    def calculate_maintenance_cost(self, db_manager):
        sql = "SELECT number_of_strings FROM guitars WHERE model_name = %s"
        db_manager.cursor.execute(sql, (self.model_name,))
        result = db_manager.cursor.fetchone()
        if result:
            number_of_strings = result[0]
            cost = number_of_strings * self.stringReplacementCost
            return cost
        else:
            print(f"Gitara {self.model_name} nie istnieje w bazie.")
            return 0

    def get_info(self, db_manager):
        sql = "SELECT model_name, number_of_strings, manufacturer, wood_type, played_hours FROM guitars WHERE model_name = %s"
        db_manager.cursor.execute(sql, (self.model_name,))
        result = db_manager.cursor.fetchone()
        if result:
            model_name, number_of_strings, manufacturer, wood_type, played_hours = result
            return f"Model: {model_name}, Strings: {number_of_strings}, Manufacturer: {manufacturer}, Wood Type: {wood_type}, Hours Played: {played_hours}"
        else:
            return f"Gitara {self.model_name} nie istnieje w bazie."
