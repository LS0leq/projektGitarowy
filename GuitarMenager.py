from Guitar import Guitar
import mysql.connector
class GuitarManager:
    def __init__(self, db_manager):
        self.collection = []
        self.db_manager = db_manager
        self.guitars = []
    def add_guitar(self, guitar):
        self.db_manager.add_guitar(guitar)

    def play_song_on_guitar(self, model_name, song):
        for guitar in self.collection:
            if guitar.model_name == model_name:
                guitar.play(song, self.db_manager)
                return
        print(f"Nie znaleziono gitary o nazwie modelu {model_name}.")

    def get_collection_summary(self):
        for guitar in self.collection:
            print(guitar.get_info(self.db_manager))

    def calculate_total_maintenance_cost(self, guitar_id, guitar_type):

        if (guitar_type == "electric"):
            print(
                " --- Cennik ---\n 50zł - nowe struny\n 2.5zł - koszt dodatkowej konserwacji za każdą godzinę gry powyżej 100 godzin\n")
        elif (guitar_type == "acoustic"):
            print(
                " --- Cennik ---\n 30zł - nowe struny\n 2.5zł - koszt dodatkowej konserwacji za każdą godzinę gry powyżej 100 godzin\n")
        else:
            print("Niepoprawny typ gitary.")
            return 0
        cost = self.db_manager.calculate_maintenance_cost_by_id(guitar_id, guitar_type)
        if cost == 0:
            print(f"Gitara o ID {guitar_id} nie istnieje lub brak danych do obliczenia kosztu.")
        else:
            print(f"Całkowity koszt konserwacji gitary o ID {guitar_id}: {cost:.2f} zł.")
        return cost

    def delete(self):
        self.db_manager.delete()
    def remove_guitar(self, model_name):
        self.db_manager.remove_guitar(model_name)
