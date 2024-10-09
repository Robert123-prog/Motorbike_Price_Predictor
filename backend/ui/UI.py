class UI:
    def __init__(self):
        pass

    def main_menu(self):
            print('''
                Please follow the instructions in order to predict the price of your motorcycle of choice! 
                ''')

    def ask_for_motorcycle(self):
        print('''
            Enter the name of the motorcycle you want:  ''')

    def confirmation_screen(self):
        print('''
            Are you sure you want to continue with this selection?  
            1. Yes
            2. No''')

    def exit_menu(self):
        print('''
        Invalid option! Please press 1 and try again.''')

    def ask_for_year(self):
        print('''
        Please enter the year in which the selected motorcycle was manufactured:''')

    def ask_for_seller_type(self):
        print('''
        Please enter the seller type of the motorcycle''')

    def error_screen_incorrect_seller_type(self):
        print('''
        Please enter the seller type correctly''')

    def error_screen_incorrect_year(self):
        print('''
           Please enter the year correctly''')

    def ask_for_owner_type(self):
        print('''
        Please enter the owner type correctly''')

    def ask_for_km_driven(self):
        print('''
        Please enter the amount of kilometers(km) driven correctly''')

    def ask_for_ex_showroom_price(self):
        print('''
        Please enter the ex-showroom price correctly''')