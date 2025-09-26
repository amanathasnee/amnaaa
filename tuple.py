library_books = [
    (1, "1984", "George Orwell", 1949),
    (2, "To Kill a Mockingbird", "Harper Lee", 1960),
    (3, "The Great Gatsby", "F. Scott Fitzgerald", 1925),
]
element = input("the id of book")
if element in library_books:
    print("the book is available",element)



