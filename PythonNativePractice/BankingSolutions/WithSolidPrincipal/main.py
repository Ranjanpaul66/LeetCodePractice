from bank_service import BankService
from bank_ui import BankUI

def main():
    bank_service = BankService()
    bank_ui = BankUI(bank_service)
    bank_ui.display_menu()

if __name__ == "__main__":
    main()
