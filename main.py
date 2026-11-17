from function import *
def main_menu():
  
  while True:
    print("\n==============================")
    print("   LIBRARY MANAGEMENT SYSTEM  ")
    print("==============================")
    print("1. Add New Book")
    print("2. Display All Books")
    print("3. Search for a Book")
    print("4. Register a Student")
    print("5. Issue a Book")
    print("6. Return a Book")
    print("7. Display Issued Books")
    print("8. Delete a Book")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
      add_book()
    elif choice == "2":
      display_books()
    elif choice == "3":
      search_book()
    elif choice == "4":
      register_student()
    elif choice == "5":
      issue_book()
    elif choice == "6":
      return_book()
    elif choice == "7":
      display_issued_books()
    elif choice == "8":
      delete_book()
    elif choice == "9":
      print("Exit Program")
      break
    else:
      print("Invalid choice! Please enter 1 to 9.")


main_menu()