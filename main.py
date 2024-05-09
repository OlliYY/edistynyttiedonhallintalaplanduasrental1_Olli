import categories
import rental_items
import users
import query_functions as qf
import calendar


def month_name(month_number):
    months = ["", "Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu",
              "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
    return months[month_number]

def main_menu():
    while True:
        _choice = input("Mitä haluat tehdä? (1=lisää roolit\n "
                    "2=lisää käyttäjiä\n "
                    "3=lisää kategoriat\n "
                    "4=lisää ominaisuudet\n "
                    "5=lisää tuotteita\n "
                    "6=lisää ominaisuuksia tuotteisiin\n "
                    "7=vuokraa\n"
                    "8=Hae lainauksien määrä kuukaudelta viikottain\n"
                    "9=Hae lainauksien määrä kuukaudelta päivittäin\n"
                    "10=Hae lainauksien määrä vuodelta kuukausittain\n"
                    "11=Hae kaikkien aikojen top 10 lainatuimmat tavarat\n"
                    "12=Hae vuoden top 10 lainatut tavarat kuukausittain\n"
                    "13=Selvitä missä kuussa tavaroita lisätään eniten valituna vuonna\n"
                    "q=lopeta): ")
        if _choice == 'q':
            break

        elif _choice == '1':
            print("lisätään roolit")
            users.insert_roles()
        elif _choice == '2':
            num_of_rows = input("Kuinka monta käyttäjää? (oletuksena 10): ")
            if num_of_rows == "":
                num_of_rows = 10
            else:
                num_of_rows = int(num_of_rows)
            users.insert_users(num_of_rows)

        elif _choice == '3':
            categories.insert_categories()

        elif _choice == '4':
            rental_items.insert_features()

        elif _choice == '5':
            rental_items.insert_items()

        elif _choice == '6':
            rental_items.mix_features_and_items()

        elif _choice == '7':
            rental_items.rent_items()



        elif _choice == '8':
            year = int(input("Syötä vuosi: "))
            month = int(input("Syötä kuukausi (1-12): "))
            month_str = month_name(month)
            results = qf.get_rentals_by_month_and_week(year, month)
            for week, count in results:
                print(f"Viikko {week} kuukaudessa {month_str}, lainauksia: {count}")

        elif _choice == '9':
            year = int(input("Syötä vuosi: "))
            month = int(input("Syötä kuukausi (1-12): "))
            month_str = month_name(month)
            results = qf.get_rentals_by_day(year, month)
            for day, count in results:
                print(f"Päivä {day} kuukaudessa {month_str}, lainauksia: {count}")

        elif _choice == '10':
            year = int(input("Syötä vuosi: "))
            results = qf.get_rentals_by_year(year)
            for month_num, count in results:
                month_str = month_name(month_num)
                print(f"Kuukausi {month_str}, lainauksia: {count}")

        elif _choice == '11':
            results = qf.get_top_rented_items_all_time()
            for item_id, name, count in results:
                print(f"Tavaran nimi: {name}, lainauksia: {count}")


        elif _choice == '12':
            year = int(input("Syötä vuosi: "))
            results = qf.get_top_rented_items_by_year_and_month(year)
            for month_num, name, count in results:
                month_str = month_name(month_num)
                print(f"Kuukausi {month_str}, Tavaran nimi: {name}, lainauksia: {count}")


        elif _choice == '13':
            year = int(input("Syötä vuosi: "))
            results = qf.get_month_most_items_added(year)
            for month_num, count in results:
                month_str = month_name(month_num)
                print(f"Eniten tavaroita lisätty kuukausi {month_str}, tuotteita lisätty: {count}")


if __name__ == "__main__":
    main_menu()

