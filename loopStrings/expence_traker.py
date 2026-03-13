#Expense Tracker

expences = []

def add_expences():
    name = input("Enter expense name: ")
    amount = input("enter expense amount: ")
    expence = {
        "name": name,
        "amount": amount
    }
    expences.append(expence)
    print("Expence added successfully!")

def view_expences():
    for expence in expences:
        print(expence["name"], "-", expence["amount"])

def show_menu():
    print("1. Add Expence")
    print("2. View Expences")
    print("3. Exit")    

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expences()
        elif choice == "2":
            view_expences()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()