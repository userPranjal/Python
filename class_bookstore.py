class BookStore:
    
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}")
        print("No of Books : ",self.NoOfBooks)

Bobj1 = BookStore("Linux System Programming", "Robert Love")
Bobj1.Display()
print()

Bobj2 = BookStore("C Programming", "Dennis Ritchie")
Bobj2.Display()
print()

Bobj3 = BookStore("An Introduction to Python", "Guido van Rossum")
Bobj3.Display()