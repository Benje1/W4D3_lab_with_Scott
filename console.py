import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Ian", "Rankin")
book1 = Book("Exit Music", author1)
author_repository.save(author1)
book_repository.save(book1)

book2 = Book("knots and Crosses", author1)
book_repository.save(book2)



pdb.set_trace()