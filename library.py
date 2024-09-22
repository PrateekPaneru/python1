class library:
    def __init__(self, listofbooks):
        self.books= listofbooks

    def booksavailable(self):
        print("the books available are:")
        for book in self.books:
            print(f" \t *{book}")

    def borrowbook(self ,bookname):
        if(bookname in self.books):
            print(f"you issued {bookname} . thanks")
            self.books.remove(bookname)
            return True
        else:
            print(f"sorry this book -{bookname} is issued by someone else")
            return False
    
    def returnbook(self,bookname):
        self.books.append(bookname)
        print(f"thanks for returning the book-{bookname}")

class student:
    def requestbook(self):
        self.book= input("enter the name you want to issue:")
        return self.book
    
    def returnbook(self):
        self.book= input("enter the name you want to return:")
        return self.book
    
    

if __name__=="__main__":
    a=library(["python" , "maths" ,"computer" , "english"])
    b=student()
    while(True):
        mac=('''-----welcome to the central library
            press for following options
            1-list of books
            2- borrow book
            3-add/return book
            4- exit the library''')
        print(mac)
        c=int(input("enter your option:"))

        if(c==1):
            a.booksavailable()
        elif(c==2):
            a.borrowbook(b.requestbook())
        elif(c==3):
            a.returnbook(b.returnbook()) 
        elif(c==4):
            print("thanks for using thsi library")
            exit()
        else:
            ("invalid option")