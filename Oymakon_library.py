class Library:
    def __init__(self,name,books):
        self.name = name
        self.books = books
        
    def append1(self,Book):
        self.books.append(Book)
    
    def search(self,author):
        found = []
        for book in self.books:
                if book.author == author:
                       found.append(book)
        return found

    def information(self,name):
        for book in self.books:
                if book.name == name:
                    print(book)

    def delete(self,author):
        new_books = []
        for book in self.books:
            if book.author != author:
                new_books.append(book)
        self.books = new_books

class Book:
    def __init__(self, name, author, distr, date, isbn):
        self.name = name
        self.author = author
        self.distr = distr
        self.date = date
        self.isbn = isbn

    def __str__(self):
        return f"Книга:{self.name}\n Автор: {self.author}\n Издательство:{self.distr}\n Год публикации:{self.date}\n Номер:{self.isbn}"

def test_library():
    anna_kar = Book('Анна Каренина','Лев Толстой','ООО Классное издательство','1875','978-5-444-48700-6' )
    war_and_piece = Book('Война и мир','Лев Толстой','ООО Плохое издательство','1865','978-5-444-48700-5')
    kazaks = Book('Казаки','Лев Толстой','ООО Очень плохое издательство','1862','978-5-444-48700-4')
    math = Book('Введение в вычислительную математику','Виктор Рябенький','2008','ФИЗМАТЛИТ','978-5-9221-0926-0')
    library = Library('Оймяконская библиотека',[])
    library.append1(anna_kar)
    library.append1(war_and_piece)
    library.append1(kazaks)
    library.append1(math)
    for book in library.books:
        name = book.name
        library.information(name)
    library.delete('Лев Толстой')
    print('Проверка!')
    for book in library.books:
        name = book.name
        library.information(name)
if __name__ == '__main__':
    test_library()
