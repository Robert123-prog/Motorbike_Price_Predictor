import joblib
import pandas as pd
from backend.helpers.Helper import Helper
from backend.ui.UI import UI

class Controller:
    def __init__(self):
        self.regressor = joblib.load(
            'model/trained_model.pkl')
        self.preprocessor = joblib.load(
            'model/preprocessor.pkl')
        self.dataset = pd.read_csv(
            'model/BIKE DETAILS.csv')

        motorcycle_names = self.dataset.iloc[:, 0]
        self.motorcycles = {i + 1: name.strip() for i, name in enumerate(motorcycle_names)}
        self.years = set(self.dataset.iloc[:, 2])
        self.seller_type = set(self.dataset.iloc[:, 3])
        self.owner_type = set(self.dataset.iloc[:, 4])
        self.helper = Helper(self.motorcycles)
        self.ui = UI()

        with open('Motorcycles', 'w') as f:
            index = 1
            for motorcycle in self.motorcycles.values():
                f.write(str(index) + ' ' + motorcycle + '\n')
                index = index + 1


    def run(self):
        motorcycle = self.select_motorcycle()
        motorcycle_year = self.select_motorcycle_year(motorcycle)
        motorcycle_seller_type = self.select_seller_type(motorcycle)
        motorcycle_owner_type = self.select_owner_type(motorcycle)
        motorcycle_km_driven = self.enter_km_driven()
        motorcycle_ex_showroom_price = self.enter_ex_showroom_price()

        input_data = pd.DataFrame({
            'name': [motorcycle],
            'year': [motorcycle_year],
            'seller_type': [motorcycle_seller_type],
            'owner': [motorcycle_owner_type],
            'km_driven': [motorcycle_km_driven],
            'ex_showroom_price': [motorcycle_ex_showroom_price]
        })

        processed_input_data = self.preprocessor.transform(input_data)
        predicted_selling_price = self.regressor.predict(processed_input_data)

        # If predicted_selling_price is a single-element array, extract the value
        if len(predicted_selling_price) == 1:
            predicted_price = predicted_selling_price[0]
            print(f'The expected selling price is: {predicted_price:.2f}')
        else:
            # Handle the case for multiple predictions
            print(f'The expected selling prices are: {predicted_selling_price}')

    def select_motorcycle(self):
        self.ui.ask_for_motorcycle()
        motorcycle = input()

        if motorcycle not in self.motorcycles.values():
            print('Motorcycle not found! Here are alternative results, please select one: ')
            self.helper.search_for_motorcycle(motorcycle)
            motorcycle_number = int(input('Please select the number of the motorcycle you would like to use: '))
            motorcycle = self.helper.return_motorcycle_from_associated_number(motorcycle_number)

            print('The chosen motorcycle is: ' + motorcycle)

            self.ui.confirmation_screen()
            user_choice = int(input())

            if user_choice == 1:
                return motorcycle

            elif user_choice == 2:
                self.select_motorcycle()
            else:
                self.ui.exit_menu()

        else:
            return motorcycle

    def select_motorcycle_year(self, motorcycle):
        self.ui.ask_for_year()
        years = {i + 1: int(year) for i, year in enumerate(self.helper.find_motorcycle_years(motorcycle))}

        print('Please select on of the available years!')
        print(years)
        motorcycle_year = int(input())

        if motorcycle_year not in years.keys():
            print('The selected year is not available for the motorcycle')
            self.select_motorcycle_year(motorcycle)

        return years.get(motorcycle_year)

    def select_seller_type(self, motorcycle):
        self.ui.ask_for_seller_type()
        seller_types = {i + 1: seller_type.strip() for i, seller_type in enumerate(self.helper.find_motorcycle_seller_type(motorcycle))}

        print('Please select on of the available seller types!')
        print(seller_types)
        motorcycle_seller_type = int(input())

        if motorcycle_seller_type not in seller_types.keys():
            print('The selected seller type is not available for the motorcycle')
            self.select_seller_type(motorcycle)

        return seller_types.get(motorcycle_seller_type)

    def select_owner_type(self, motorcycle):
        self.ui.ask_for_owner_type()
        owner_types = {i + 1: owner_type.strip() for i, owner_type in enumerate(self.helper.find_motorcycle_owner_type(motorcycle))}

        print('Please select on of the available owner types!')
        print(owner_types)
        motorcycle_owner_type = int(input())

        if motorcycle_owner_type not in owner_types.keys():
            print('The selected owner type is not available for the motorcycle')
            self.select_owner_type(motorcycle)

        return owner_types.get(motorcycle_owner_type)

    def enter_km_driven(self):
        self.ui.ask_for_km_driven()
        motorcycle_km_driven = int(input())
        return motorcycle_km_driven

    def enter_ex_showroom_price(self):
        self.ui.ask_for_ex_showroom_price()
        motorcycle_ex_showroom_price = int(input())
        return motorcycle_ex_showroom_price




