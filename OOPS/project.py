from abc import ABC, abstractmethod



class Library(ABC):

    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def view_book(self):
        pass

    @abstractmethod
    def issue_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def delete_book(self):
        pass



class College(Library):

    def __init__(self,a):

        self.book_store = a

    def add_book(self):

        if self.book_store == []:

            count = int(input("How many books do you want to add: "))

            for i in range(count):

                book_name = input("Enter book name: ")
                self.book_store.append(book_name)

            print("Books added successfully.")

        else:
            book_name = input("Enter book name: ")
            self.book_store.append(book_name)
            print("Book added successfully.")


    def view_book(self):

        if self.book_store == []:

            print("No books available.")
        else:
            print("Available books are: ")

            # for i in self.book_store:
            #     print(i)

            for Sno, Name in enumerate(self.book_store,start=101):
                print(f"{Sno}. {Name}")
                
    def issue_book(self):
       
       issue_book_name = input("Enter book name to issue: ")

       if issue_book_name in self.book_store:
           
           print(f"You have issued {issue_book_name} book successfully.")

           self.book_store.remove(issue_book_name)

       else:
           print("Book not available.")    

    def return_book(self):
        
        return_book_name = input("Enter Book name to return: ")
        self.book_store.append(return_book_name)
        print(f"You have returned {return_book_name} book successfully.")
        

    def delete_book(self):

        delete_book_name = input("Enter book name to delete: ")

        if delete_book_name in self.book_store:

            self.book_store.remove(delete_book_name)
            print(f"{delete_book_name} book deleted successfully.")

        else:
            print("Book not available.")

book_store = []

obj = College(book_store)


while True:

    print("1. Add Book")
    print("2. View Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        obj.add_book()

    elif option == 2:
        obj.view_book()

    elif option == 3:
        obj.issue_book()

    elif option == 4:
        obj.return_book()

    elif option == 5:
        obj.delete_book()

    elif option == 6:
        print("Thank you for using the library management system.")
        break
    else:
        print("Invalid option. Please try again.")