class BookStore:
    
    No_Of_Books = 0

    def __init__(self,Name,Author):
        self.Name = Name 
        self.Author = Author
    
    def Display(self):
        print(f"Book Name {self.Name} By Author {self.Author}")
        print(f"Number of the Books : {BookStore.No_Of_Books + 1}")

Obj1 = BookStore("Linux System Programming","Robert Love")
Obj1.Display()


    