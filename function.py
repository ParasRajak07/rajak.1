from database import load_data,save_data
def add_book():
  books = load_data("books.json")
  print("\n--- Add New Book ---")
  book_id = input("Enter Book ID: ")

  for b in books:
    if b["book_id"].lower() == book_id.lower():
      print("Book ID already exists!")
      return

  book_name = input("Enter Book Name: ")
  author = input("Enter Author Name: ")
  category = input("Enter Category: ")
  copies_input = input("Enter Number of Copies: ")

  if copies_input.isdigit() == False:
    print("Error: Please enter a valid number!")
    return

  copies = int(copies_input)
  if copies <= 0:
    print("Error: Copies must be greater than zero!")
    return

  new_book = {
      "book_id": book_id,
      "book_name": book_name,
      "author": author,
      "category": category,
      "available_copies": copies,
  }

  books.append(new_book)
  save_data("books.json", books)
  print("Book added successfully!")

def display_books():
    books = load_data("books.json")

    if len(books) == 0:
        print("No books available.")
        return
    print(
        f"{'ID':<10} | {'Book Name':<20} | {'Author':<15} | {'Category':<12} |"
        f" {'Copies':<6}"
    )
    print("-" * 72)
    for b in books:
        print(
            f"{str(b.get('book_id', '')):<10} |"
            f" {str(b.get('book_name', '')):<20} |"
            f" {str(b.get('author', '')):<15} |"
            f" {str(b.get('category', '')):<12} |"
            f" {b.get('available_copies', 0)}"
        )    
def search_book():
  books = load_data("books.json")
  if len(books) == 0:
    print("\nNo books available to search.")
    return

  print("\n--- Search Book ---")
  search_text = input("Enter Book ID, Book Name, or Author Name: ").lower()
  Unsucessful= False

  for b in books:
    if (
        search_text in b["book_id"].lower()
        or search_text in b["book_name"].lower()
        or search_text in b["author"].lower()
    ):
      print(
          "ID:",
          b["book_id"],
          "| Name:",
          b["book_name"],
          "| Author:",
          b["author"],
          "| Category:",
          b["category"],
          "| Copies:",
          b["available_copies"],
      )
      Unsucessful = True

  if Unsucessful == False:
    print("No matching book found.")

def register_student():
  students = load_data("students.json")
  print("\n--- Register a Student ---")
  student_id = input("Enter Student ID: ")

  for s in students:
    if s["student_id"].lower() == student_id.lower():
      print("Error: Student ID already registered!")
      return

  student_name = input("Enter Student Name: ")
  department = input("Enter Department: ")
  contact = input("Enter Contact Number: ")

  new_student = {
      "student_id": student_id,
      "student_name": student_name,
      "department": department,
      "contact": contact,
  }

  students.append(new_student)
  save_data("students.json", students)
  print("Student registered successfully!")

def issue_book():
  books = load_data("books.json")
  students = load_data("students.json")
  issued_books = load_data("issued_books.json")

  print("\n--- Issue a Book ---")
  student_id = input("Enter Student ID: ")

  student_founded = False
  for s in students:
    if s["student_id"].lower() == student_id.lower():
      student_founded = True
      break

  if student_founded == False:
    print("Error: Student is not registered!")
    return
  
  total_issued = 0
  for r in issued_books:
    if r["student_id"].lower() == student_id.lower():
      total_issued = total_issued + 1

  if total_issued >= 3:
    print("Error: Student already has 3 books issued!")
    return

  book_id = input("Enter Book ID: ")
  book_founded = False

  for b in books:
    if b["book_id"].lower() == book_id.lower():
      book_founded = True
      if b["available_copies"] > 0:
        issue_date = input("Enter Issue Date (DD-MM-YYYY): ")
        b["available_copies"] = b["available_copies"] - 1

        new_issue = {
            "student_id": student_id,
            "book_id": book_id,
            "issue_date": issue_date,
        }
        issued_books.append(new_issue)

        save_data("books.json", books)
        save_data("issued_books.json", issued_books)
        print("Book issued successfully!")
      else:
        print("Error: No copies available!")
      break

  if book_founded == False:
    print("Error: Book ID not found!")

def return_book():
  books = load_data("books.json")
  issued_books = load_data("issued_books.json")

  print("\n--- Return a Book ---")
  student_id = input("Enter Student ID: ")
  book_id = input("Enter Book ID: ")

  record_Founded = False
  i = 0
  while i < len(issued_books):
    if (
        issued_books[i]["student_id"].lower() == student_id.lower()
        and issued_books[i]["book_id"].lower() == book_id.lower()
    ):
      issued_books.pop(i)
      record_Founded = True
      break
    i = i + 1

  if record_Founded == False:
    print("Error: Issue record not found!")
    return

  for b in books:
    if b["book_id"].lower() == book_id.lower():
      b["available_copies"] = b["available_copies"] + 1
      break

  save_data("books.json", books)
  save_data("issued_books.json", issued_books)
  print("Book returned successfully!")

def display_issued_books():
  issued_books = load_data("issued_books.json")
  students = load_data("students.json")

  print("\n--- Currently Issued Books ---")
  print("Total Registered Students:", len(students))
  print("Total Currently Issued Books:", len(issued_books))

  if len(issued_books) == 0:
    print("No books are currently issued.")
    return

  print("Student ID | Book ID | Issue Date")
  print("-------------------------------------")
  for r in issued_books:
    print(r["student_id"], "|", r["book_id"], "|", r["issue_date"])

def delete_book():
  books = load_data("books.json")
  issued_books = load_data("issued_books.json")

  print("\n--- Delete a Book ---")
  book_id = input("Enter Book ID to delete: ")

  for r in issued_books:
    if r["book_id"].lower() == book_id.lower():
      print("Error: Cannot delete! Book is currently issued.")
      return

  i = 0
  while i < len(books):
    if books[i]["book_id"].lower() == book_id.lower():
      books.pop(i)
      save_data("books.json", books)
      print("Book deleted successfully!")
      return
    i = i + 1

  print("Error: Book ID not found!")

