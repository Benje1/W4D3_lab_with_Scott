import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Ian", "Rankin")
book1 = Book("Exit Music", author1)


pdb.set_trace()