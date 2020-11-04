from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Roald", "Dahl")
author2 = Author("Stephen", "King")

author_repository.save(author1)
author_repository.save(author2)

book1 = Book("Matilda", "Fantasy", author1)
book2 = Book("The Shining", "Horror", author2)
book3 = Book("Carrie", "Horror", author2)

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)

