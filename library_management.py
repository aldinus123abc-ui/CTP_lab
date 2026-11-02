class LibraryItem:
    def __init__(self, item_id, title, author):
        self._item_id = item_id
        self._title = title
        self._author = author
        self._is_issued = False

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def is_issued(self):
        return self._is_issued

    def issue_item(self):
        if not self._is_issued:
            self._is_issued = True
            return True
        return False

    def return_item(self):
        if self._is_issued:
            self._is_issued = False
            return True
        return False

    def get_item_details(self):
        raise NotImplementedError("Subclasses must implement abstract method")


class Book(LibraryItem):
    def __init__(self, item_id, title, author, isbn, pages):
        super().__init__(item_id, title, author)
        self.isbn = isbn
        self.pages = pages

    def get_item_details(self):
        status = "Checked Out" if self._is_issued else "Available"
        return f"[Book] ID: {self._item_id} | Title: '{self._title}' | Author: {self._author} | ISBN: {self.isbn} | Pages: {self.pages} | Status: {status}"


class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue_number, month):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number
        self.month = month

    def get_item_details(self):
        status = "Checked Out" if self._is_issued else "Available"
        return f"[Magazine] ID: {self._item_id} | Title: '{self._title}' | Publisher: {self._author} | Issue: #{self.issue_number} ({self.month}) | Status: {status}"


class Journal(LibraryItem):
    def __init__(self, item_id, title, author, volume, field_of_study):
        super().__init__(item_id, title, author)
        self.volume = volume
        self.field_of_study = field_of_study

    def get_item_details(self):
        status = "Checked Out" if self._is_issued else "Available"
        return f"[Journal] ID: {self._item_id} | Title: '{self._title}' | Researcher: {self._author} | Vol: {self.volume} | Field: {self.field_of_study} | Status: {status}"


class LibrarySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item: LibraryItem):
        if item.item_id in self.inventory:
            print(f"Error: Item ID {item.item_id} already exists.")
        else:
            self.inventory[item.item_id] = item
            print(f"Successfully added: {item.title}")

    def display_inventory(self):
        print("\n--- Current Library Inventory ---")
        if not self.inventory:
            print("Library is empty.")
            return
        for item in self.inventory.values():
            print(item.get_item_details())
        print("-" * 35)

    def issue_item(self, item_id):
        item = self.inventory.get(item_id)
        if not item:
            print(f"Error: Item with ID {item_id} not found.")
            return
        
        if item.issue_item():
            print(f"Success: '{item.title}' has been issued.")
        else:
            print(f"Failure: '{item.title}' is already issued.")

    def return_item(self, item_id):
        item = self.inventory.get(item_id)
        if not item:
            print(f"Error: Item with ID {item_id} not found.")
            return
        
        if item.return_item():
            print(f"Success: '{item.title}' has been returned.")
        else:
            print(f"Failure: '{item.title}' was not checked out.")


if __name__ == "__main__":
    my_library = LibrarySystem()

    book1 = Book("B001", "Clean Code", "Robert C. Martin", "978-0132350884", 464)
    mag1 = Magazine("M001", "Wired", "Condé Nast", 304, "July 2026")
    journal1 = Journal("J001", "Quantum Computing Letters", "Dr. Richard Feynman", 8, "Physics")

    print("--- Adding Items ---")
    my_library.add_item(book1)
    my_library.add_item(mag1)
    my_library.add_item(journal1)

    my_library.display_inventory()

    print("\n--- Testing Issue & Return ---")
    my_library.issue_item("B001")  
    my_library.issue_item("B001") 
    
    my_library.display_inventory()

    my_library.return_item("B001") 
    my_library.display_inventory()