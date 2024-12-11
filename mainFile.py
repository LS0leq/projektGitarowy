from GuitarMenager import GuitarManager
from Electric import ElectricGuitar
from Acoustic import AcousticGuitar
from DatabaseManager import GuitarDatabaseManager

def display_menu():
    print("\n--- Guitar Collection Manager ---")
    print("1. Dodaj gitarę ELEKTRYCZNĄ")
    print("2. Dodaj gitarę AKUSTYCZNĄ")
    print("3. Usuń gitarę")
    print("4. Pokaż kolekcję gitar")
    print("5. Przelicz koszt konserwacji")
    print("6. Usuń dane z bazy danych")
    print("7. Exit")

def get_electric_guitar_details():
    model_name = input("Wprowadź nazwę modelu: ")
    number_of_strings = int(input("Podaj ilość strun: "))
    manufacturer = input("Podaj producenta: ")
    pickup_type = input("Podaj rodzaj pickupu: ")
    played_hours = int(input("Podaj ilość godzin: "))
    return ElectricGuitar(model_name, number_of_strings, manufacturer, pickup_type, played_hours)

def get_acoustic_guitar_details():
    model_name = input("Wprowadź nazwę modelu: ")
    number_of_strings = int(input("Podaj ilość strun: "))
    manufacturer = input("Podaj producenta: ")
    played_hours = int(input("Podaj ilość godzin: "))
    wood_type = input("Podaj rodzaj drewna: ")
    return AcousticGuitar(model_name, number_of_strings, manufacturer,wood_type,played_hours, )

if __name__ == "__main__":
    db_manager = GuitarDatabaseManager()
    manager = GuitarManager(db_manager)
    print("")
    print("< --- Witaj w programie Guitar Collection Manager! --- >")
    while True:
        display_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            electric_guitar = get_electric_guitar_details()
            manager.add_guitar(electric_guitar)
            print("Dodano gitarę pomyślnie!")

        elif choice == "2":
            acoustic_guitar = get_acoustic_guitar_details()
            manager.add_guitar(acoustic_guitar)
            print("Dodano gitarę pomyślnie!")


        elif choice == "3":
            model_name = input("Podaj ID gitary do usunięcia: ")
            manager.remove_guitar(int(model_name))
            print(f"Gitara '{model_name}' usunięta!")

        elif choice == "4":
            db_manager.get_guitar_info()



        elif choice == "5":

            guitar_id = int(input("Podaj ID gitary, dla której chcesz obliczyć koszt konserwacji: "))

            guitar_type = int(input("1 - Elektryczna, 2 - Akustyczna: "))

            if guitar_type == 1:

                total_cost = manager.calculate_total_maintenance_cost(guitar_id, "electric")

                print(f"Łączny koszt konserwacji gitary elektrycznej o ID {guitar_id}: {total_cost:.2f} zł")

            elif guitar_type == 2:

                total_cost = manager.calculate_total_maintenance_cost(guitar_id, "acoustic")

                print(f"Łączny koszt konserwacji gitary akustycznej o ID {guitar_id}: {total_cost:.2f} zł")

            else:

                print("Nieprawidłowy wybór, spróbuj ponownie.")


        elif choice == "6":
            manager.delete()
            print(f"Usunięto dane z basy danych")

        elif choice == "7":
            print("Zamykam program...")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
