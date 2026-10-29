"""
Mini Project: Library Management System
---------------------------------------
Concepts used:
  * Classes & objects ........ Book, Member, PremiumMember, Library
  * Constructors (__init__) .. every class
  * Instance methods ......... borrow, return, display, search
  * Encapsulation ............ private attributes (__is_available, __borrowed_books,
                               __borrowing_history) changed only through methods
  * Inheritance .............. PremiumMember(Member)
  * Method overriding ........ get_borrow_limit() in PremiumMember
  * Dictionary ............... books / members stored by unique ID
  * List ..................... borrowed book IDs and borrowing history
  * Set ...................... unique genres (and set operations on preferred genres)
  * Tuple .................... fixed categories and membership types

Run normally:        python library_management_system.py
Run sample scenario: python library_management_system.py --demo
"""

import sys

# ----------------------------------------------------------------------
# TUPLES: fixed values that never change
# ----------------------------------------------------------------------
BOOK_CATEGORIES = ("Fiction", "Science", "History", "Biography", "Programming")
MEMBERSHIP_TYPES = ("Standard", "Premium")


# ======================================================================
# CLASS 1: Book
# ======================================================================
class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.__is_available = True          # private (encapsulated)

    # read-only access to availability
    @property
    def is_available(self):
        return self.__is_available 

    def display_details(self):
        status = "Available" if self.__is_available else "Borrowed"
        print(f"{self.book_id:<8}{self.title:<30}{self.author:<22}"
              f"{self.genre:<14}{status}")

    def borrow_book(self):
        """Mark book as unavailable. Returns True if it worked."""
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        """Mark book as available. Returns True if it worked."""
        if not self.__is_available:
            self.__is_available = True
            return True
        return False


# ======================================================================
# CLASS 2: Member
# ======================================================================
class Member:
    STANDARD_LIMIT = 2

    def __init__(self, member_id, name, preferred_genres=None):
        self.member_id = member_id
        self.name = name
        self.membership_type = MEMBERSHIP_TYPES[0]      # "Standard"
        self.preferred_genres = set(preferred_genres) if preferred_genres else set()
        self.__borrowed_books = []          # LIST of book IDs (private)
        self.__borrowing_history = []       # LIST of (book_id, title) returned

    # read-only views (copies, so outside code cannot modify the originals)
    @property
    def borrowed_books(self):
        return list(self.__borrowed_books)

    @property
    def borrowing_history(self):
        return list(self.__borrowing_history)

    def get_borrow_limit(self):
        """Standard members may borrow 2 books (overridden in PremiumMember)."""
        return Member.STANDARD_LIMIT

    def display_details(self):
        print(f"{self.member_id:<8}{self.name:<22}{self.membership_type:<12}"
              f"Borrowed now: {len(self.__borrowed_books)}/{self.get_borrow_limit()}")

    def borrow_book(self, book):
        """Returns (success: bool, message: str)."""
        if len(self.__borrowed_books) >= self.get_borrow_limit():
            return False, (f"{self.name} has reached the borrowing limit "
                           f"of {self.get_borrow_limit()} book(s).")
        if not book.is_available:
            return False, f"'{book.title}' is currently not available."
        book.borrow_book()                          # mark unavailable
        self.__borrowed_books.append(book.book_id)  # add to current list
        return True, f"{self.name} borrowed '{book.title}'."

    def return_book(self, book):
        """Returns (success: bool, message: str)."""
        if book.book_id not in self.__borrowed_books:
            return False, f"{self.name} has not borrowed '{book.title}'."
        book.return_book()                                      # mark available
        self.__borrowed_books.remove(book.book_id)              # remove from current
        self.__borrowing_history.append((book.book_id, book.title))  # add to history
        return True, f"{self.name} returned '{book.title}'."

    def display_borrowed_books(self, library_books):
        if not self.__borrowed_books:
            print(f"{self.name} has no books currently borrowed.")
            return
        print(f"Books currently borrowed by {self.name}:")
        for bid in self.__borrowed_books:
            print(f"  - {bid}: {library_books[bid].title}")

    def display_history(self):
        if not self.__borrowing_history:
            print(f"{self.name} has no borrowing history yet.")
            return
        print(f"Borrowing history of {self.name}:")
        for bid, title in self.__borrowing_history:
            print(f"  - {bid}: {title}")


# ======================================================================
# CLASS 3: PremiumMember (inherits Member)
# ======================================================================
class PremiumMember(Member):
    PREMIUM_LIMIT = 5

    def __init__(self, member_id, name, preferred_genres=None):
        super().__init__(member_id, name, preferred_genres)
        self.membership_type = MEMBERSHIP_TYPES[1]      # "Premium"
        self.membership_fee = 800  #

    # METHOD OVERRIDING
    def get_borrow_limit(self):
        return PremiumMember.PREMIUM_LIMIT

    def display_details(self):
        super().display_details()
        print(f"        Membership fee: {self.membership_fee}")


# ======================================================================
# Library (manages everything)
# ======================================================================
class Library:
    def __init__(self, name="City Library"):
        self.name = name
        self.books = {}         # DICTIONARY: book_id -> Book object
        self.members = {}       # DICTIONARY: member_id -> Member object
        self.genres = set()     # SET: unique genres

    # ---------------- Book management ----------------
    def add_book(self, book_id, title, author, genre):
        if book_id in self.books:                       # prevent duplicate IDs
            print(f"Error: Book ID '{book_id}' already exists.")
            return False
        self.books[book_id] = Book(book_id, title, author, genre)
        self.genres.add(genre)
        print(f"Book '{title}' added successfully.")
        return True

    @staticmethod
    def _print_book_header():
        print(f"{'ID':<8}{'Title':<30}{'Author':<22}{'Genre':<14}Status")
        print("-" * 82)

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        self._print_book_header()
        for book in self.books.values():
            book.display_details()

    def search_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            self._print_book_header()
            book.display_details()
        else:
            print(f"No book found with ID '{book_id}'.")

    def search_book_by_title(self, keyword):
        found = [b for b in self.books.values() if keyword.lower() in b.title.lower()]
        if found:
            self._print_book_header()
            for book in found:
                book.display_details()
        else:
            print(f"No book found with title containing '{keyword}'.")

    def display_books_by_genre(self, genre):
        found = [b for b in self.books.values() if b.genre.lower() == genre.lower()]
        if found:
            self._print_book_header()
            for book in found:
                book.display_details()
        else:
            print(f"No books found in genre '{genre}'.")

    def display_available_books(self):
        available = [b for b in self.books.values() if b.is_available]
        if available:
            self._print_book_header()
            for book in available:
                book.display_details()
        else:
            print("No books are currently available.")

    def display_all_genres(self):
        if not self.genres:
            print("No genres available yet.")
            return
        print("Unique genres in the library:")
        for genre in sorted(self.genres):
            print(f"  - {genre}")

    def common_genres(self, member_id_1, member_id_2):
        """SET operation: intersection of two members' preferred genres."""
        m1, m2 = self.members.get(member_id_1), self.members.get(member_id_2)
        if not m1 or not m2:
            print("Both member IDs must exist.")
            return
        common = m1.preferred_genres & m2.preferred_genres
        print(f"Common preferred genres of {m1.name} and {m2.name}: "
              f"{sorted(common) if common else 'None'}")

    # ---------------- Member management ----------------
    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Error: Member ID '{member.member_id}' already exists.")
            return False
        self.members[member.member_id] = member
        print(f"{member.membership_type} member '{member.name}' registered successfully.")
        return True

    def display_all_members(self):
        if not self.members:
            print("No members registered.")
            return
        for member in self.members.values():
            member.display_details()

    def search_member(self, member_id):
        member = self.members.get(member_id)
        if member:
            member.display_details()
        else:
            print(f"No member found with ID '{member_id}'.")

    def display_member_borrowed_books(self, member_id):
        member = self.members.get(member_id)
        if member:
            member.display_borrowed_books(self.books)
        else:
            print(f"No member found with ID '{member_id}'.")

    def display_member_history(self, member_id):
        member = self.members.get(member_id)
        if member:
            member.display_history()
        else:
            print(f"No member found with ID '{member_id}'.")

    # ---------------- Borrow / Return ----------------
    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member is None:
            print(f"Error: Member '{member_id}' does not exist.")
        elif book is None:
            print(f"Error: Book '{book_id}' does not exist.")
        else:
            success, message = member.borrow_book(book)
            print(("Success: " if success else "Error: ") + message)

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member is None:
            print(f"Error: Member '{member_id}' does not exist.")
        elif book is None:
            print(f"Error: Book '{book_id}' does not exist.")
        else:
            success, message = member.return_book(book)
            print(("Success: " if success else "Error: ") + message)


# ======================================================================
# Input helpers
# ======================================================================
def ask(prompt):
    """Ask for non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


# ======================================================================
# Menu actions
# ======================================================================
def menu_add_book(lib):
    print("Suggested categories:", ", ".join(BOOK_CATEGORIES))
    book_id = ask("Book ID: ").upper()
    if book_id in lib.books:
        print(f"Error: Book ID '{book_id}' already exists.")
        return
    title = ask("Title: ")
    author = ask("Author: ")
    genre = ask("Genre: ").title()
    lib.add_book(book_id, title, author, genre)


def menu_search_book(lib):
    print("Search by: 1. Book ID   2. Title   3. Genre")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        lib.search_book_by_id(ask("Enter Book ID: ").upper())
    elif choice == "2":
        lib.search_book_by_title(ask("Enter title (or part of it): "))
    elif choice == "3":
        lib.display_books_by_genre(ask("Enter genre: "))
    else:
        print("Invalid choice.")


def menu_register_member(lib):
    member_id = ask("Member ID: ").upper()
    if member_id in lib.members:
        print(f"Error: Member ID '{member_id}' already exists.")
        return
    name = ask("Name: ")
    print("Membership types:", ", ".join(MEMBERSHIP_TYPES))
    m_type = ask("Membership type: ").title()
    if m_type not in MEMBERSHIP_TYPES:
        print("Invalid membership type. Registration cancelled.")
        return
    raw = input("Preferred genres (comma separated, optional): ")
    prefs = {g.strip().title() for g in raw.split(",") if g.strip()}
    if m_type == "Premium":
        fee = ask_float("Membership fee: ")
        member = PremiumMember(member_id, name, fee, prefs)
    else:
        member = Member(member_id, name, prefs)
    lib.register_member(member)


def menu_display_members(lib):
    print("1. Display all members   2. Search member by ID   3. Common genres of two members")
    choice = input("Choose (1-3): ").strip()
    if choice == "1":
        lib.display_all_members()
    elif choice == "2":
        lib.search_member(ask("Enter Member ID: ").upper())
    elif choice == "3":
        lib.common_genres(ask("First Member ID: ").upper(),
                          ask("Second Member ID: ").upper())
    else:
        print("Invalid choice.")


# ======================================================================
# Main menu
# ======================================================================
def main():
    lib = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. Display All Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Display Available Books")
        print("9. Display Borrowed Books of a Member")
        print("10. Display All Genres")
        print("11. Display Borrowing History")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ").strip()
        print()

        if choice == "1":
            menu_add_book(lib)
        elif choice == "2":
            lib.display_all_books()
        elif choice == "3":
            menu_search_book(lib)
        elif choice == "4":
            menu_register_member(lib)
        elif choice == "5":
            menu_display_members(lib)
        elif choice == "6":
            lib.borrow_book(ask("Member ID: ").upper(), ask("Book ID: ").upper())
        elif choice == "7":
            lib.return_book(ask("Member ID: ").upper(), ask("Book ID: ").upper())
        elif choice == "8":
            lib.display_available_books()
        elif choice == "9":
            lib.display_member_borrowed_books(ask("Member ID: ").upper())
        elif choice == "10":
            lib.display_all_genres()
        elif choice == "11":
            lib.display_member_history(ask("Member ID: ").upper())
        elif choice == "12":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 12.")


# ======================================================================
# Automatic run of the sample scenario (python file.py --demo)
# ======================================================================
def run_demo():
    lib = Library()
    print("--- 1. Add books ---")
    lib.add_book("B101", "Python Programming", "Guido Smith", "Programming")
    lib.add_book("B102", "Java Programming", "James Gosling", "Programming")
    lib.add_book("B103", "Database Systems", "Ramez Elmasri", "Science")
    # Extra books so the premium member can borrow 3 (only 3 books exist in the brief,
    # and the standard member already holds 2 of them)
    lib.add_book("B104", "World History", "Anna Brown", "History")
    lib.add_book("B105", "Great Biographies", "John Doe", "Biography")
    lib.add_book("B101", "Duplicate", "Nobody", "Fiction")      # duplicate ID test

    print("\n--- 2. Register members ---")
    lib.register_member(Member("M101", "Alice", {"Programming", "Science"}))
    lib.register_member(PremiumMember("M102", "Bob", 500.0, {"Science", "History"}))

    print("\n--- 3. M101 borrows 2 books, then tries a 3rd ---")
    lib.borrow_book("M101", "B101")
    lib.borrow_book("M101", "B102")
    lib.borrow_book("M101", "B103")          # should fail: limit reached

    print("\n--- 4. M102 borrows 3 books ---")
    lib.borrow_book("M102", "B103")
    lib.borrow_book("M102", "B104")
    lib.borrow_book("M102", "B105")

    print("\n--- 5. Return one book and check availability ---")
    lib.return_book("M101", "B101")
    lib.search_book_by_id("B101")

    print("\n--- 6. Borrowed books and history ---")
    for mid in ("M101", "M102"):
        lib.display_member_borrowed_books(mid)
        lib.display_member_history(mid)

    print("\n--- 7. All genres ---")
    lib.display_all_genres()

    print("\n--- Bonus: common preferred genres ---")
    lib.common_genres("M101", "M102")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        main()