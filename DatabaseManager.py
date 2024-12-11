from Acoustic import AcousticGuitar
from Electric import ElectricGuitar
import mysql.connector


class GuitarDatabaseManager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="my-secret-pw",
            database="guitar_manager"
        )
        self.cursor = self.mydb.cursor()

    def add_guitar(self, guitar):
        if isinstance(guitar, AcousticGuitar):
            sql = """
            INSERT INTO guitars (model_name, number_of_strings, manufacturer, played_hours, wood_type)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (
            guitar.model_name, guitar.number_of_strings, guitar.manufacturer, guitar.played_hours, guitar.wood_type)
        elif isinstance(guitar, ElectricGuitar):
            sql = """
            INSERT INTO guitars (model_name, number_of_strings, manufacturer, played_hours, pickup_type)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (
            guitar.model_name, guitar.number_of_strings, guitar.manufacturer, guitar.played_hours, guitar.pickup_type)

        self.cursor.execute(sql, values)
        self.mydb.commit()
        print(f"Gitarę {guitar.model_name} dodano do bazy danych.")

        self.cursor.execute("SELECT * FROM guitars WHERE model_name = %s", (guitar.model_name,))
        result = self.cursor.fetchone()
        if result:
            print("Dane gitary w bazie:", result)
        else:
            print("Nie znaleziono gitary w bazie po dodaniu!")

        self.cursor.fetchall()

    def get_guitar_info(self):
        sql = "SELECT * FROM guitars"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            for guitar in result:
                print(guitar)
        else:
            print("Nie znaleziono gitar w bazie.")

    def update_played_hours(self, model_name, hours):
        sql = "UPDATE guitars SET played_hours = played_hours + %s WHERE model_name = %s"
        self.cursor.execute(sql, (hours, model_name))
        self.mydb.commit()
    def remove_guitar(self,id):
        sql = "DELETE FROM guitars WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.mydb.commit()
    def delete(self):
        sql = "DELETE FROM guitars"
        self.cursor.execute(sql)
        self.mydb.commit()

    def calculate_maintenance_cost_by_id(self, guitar_id, guitar_type):
        sql = "SELECT played_hours, number_of_strings FROM guitars WHERE id = %s"
        self.cursor.execute(sql, (guitar_id,))
        result = self.cursor.fetchone()
        if result:
            played_hours, number_of_strings = result
            extra_hours = max(0, played_hours - 100)
            if(guitar_type == "electric"):
                string_replacement_cost = 50
            if(guitar_type == "acoustic"):
                string_replacement_cost = 40
            hourly_maintenance_cost = extra_hours * 2.5
            total_cost = string_replacement_cost + hourly_maintenance_cost
            return total_cost
        else:
            print(f"DEBUG: Gitara o ID {guitar_id} nie istnieje w bazie.")
            return 0

