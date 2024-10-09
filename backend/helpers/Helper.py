import pandas as pd
class Helper:
    def __init__(self, motorcycle_map):
        self.filename = '../controller/Motorcycles'
        self.motorcycle_map = motorcycle_map
        self.dataset = pd.read_csv(
            r'/model/BIKE DETAILS.csv'
        )

    def search_for_motorcycle(self, partial_name):
        found = False
        for number, motorcycle_name in self.motorcycle_map.items():
            if partial_name.lower() in motorcycle_name.lower():
                print(f"{number} {motorcycle_name}")
                found = True
        if not found:
            print("No motorcycles matching your query were found.")

    def return_motorcycle_from_associated_number(self, number):
        if number in self.motorcycle_map:
            return self.motorcycle_map[number]
        else:
            print('Invalid number selected.')
            return None






    def find_motorcycle_years(self, motorcycle):
        filtered_rows = self.dataset[self.dataset.iloc[:, 0].str.strip().str.lower() == motorcycle.strip().lower()]

        # Extract all years associated with that motorcycle (unique years)
        motorcycle_years = filtered_rows.iloc[:, 2].unique()

        if motorcycle_years.size > 0:
            print(f"Years available for {motorcycle}: {', '.join(map(str, motorcycle_years))}")
            return motorcycle_years
        else:
            print(f"No years found for the selected motorcycle: {motorcycle}")
            return None

    def find_motorcycle_seller_type(self, motorcycle):
        filtered_rows = self.dataset[self.dataset.iloc[:, 0].str.strip().str.lower() == motorcycle.strip().lower()]
        motorcycle_seller_types = filtered_rows.iloc[:, 3].unique()

        if motorcycle_seller_types.size > 0:
            print(f"Years available for {motorcycle}: {', '.join(map(str, motorcycle_seller_types))}")
            return motorcycle_seller_types
        else:
            print(f"No years found for the selected motorcycle: {motorcycle}")
            return None

    def find_motorcycle_owner_type(self, motorcycle):
        filtered_rows = self.dataset[self.dataset.iloc[:, 0].str.strip().str.lower() == motorcycle.strip().lower()]
        motorcycle_seller_types = filtered_rows.iloc[:, 4].unique()

        if motorcycle_seller_types.size > 0:
            print(f"Years available for {motorcycle}: {', '.join(map(str, motorcycle_seller_types))}")
            return motorcycle_seller_types
        else:
            print(f"No years found for the selected motorcycle: {motorcycle}")
            return None
