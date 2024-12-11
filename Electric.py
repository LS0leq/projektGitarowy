from Guitar import Guitar

class ElectricGuitar(Guitar):
    maxHoursBeforeMaintenance = 100
    maintenanceCostPerHour = 2.5
    stringReplacementCost = 15

    def __init__(self, model_name, number_of_strings, manufacturer, pickup_type, played_hours=0):
        super().__init__(model_name, number_of_strings, manufacturer)
        self.pickup_type = pickup_type
        self.played_hours = played_hours



    def calculate_maintenance_cost(self, db_manager):
        sql = "SELECT played_hours, number_of_strings FROM guitars WHERE model_name = %s"
        db_manager.cursor.execute(sql, (self.model_name,))
        result = db_manager.cursor.fetchone()
        if result:
            played_hours, number_of_strings = result
            extra_hours = max(0, played_hours - self.maxHoursBeforeMaintenance)
            cost = extra_hours * self.maintenanceCostPerHour + number_of_strings * self.stringReplacementCost
            return cost
        else:
            print(f"Gitara {self.model_name} nie istnieje w bazie.")
            return 0


    def get_info(self, db_manager):
        sql = "SELECT model_name, number_of_strings, manufacturer, pickup_type, played_hours FROM guitars WHERE model_name = %s"
        db_manager.cursor.execute(sql, (self.model_name,))
        result = db_manager.cursor.fetchone()
        if result:
            model_name, number_of_strings, manufacturer, pickup_type, played_hours = result
            return f"Model: {model_name}, Strings: {number_of_strings}, Manufacturer: {manufacturer}, Pickup Type: {pickup_type}, Hours Played: {played_hours}"
        else:
            return f"Gitara {self.model_name} nie istnieje w bazie."
