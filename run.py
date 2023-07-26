import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    requests input from the user for the sales of sandwiches
    """
    print("please input sales data from the last market")
    print("Data should be 6 numbers, seperated by commas")
    print("Example: 1,2,3,4,5,6\n")

    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Converts all data to integers in the above function.
    Raises ValueError if strings aren't converted to integers or more or less than 6 values
    have been input.
    """
    try:
        if len(values) != 6:
            raise ValueError(
            f"Exactly six values required you only provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")

    
    
get_sales_data()