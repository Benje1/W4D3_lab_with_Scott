from flask import Flask, render_template, Blueprint, request, redirect
from models.author import Author
from models.book import Book
from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("/books/index.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new")
def new():
    return render_template("/books/new.html")

@books_blueprint.route("/books", methods=["POST"])
def create():
    title = request.form['title']
    first = request.form['first_name']
    last = request.form['last_name']
    authors = author_repository.select_all()
    author_result = Author(first, last)
    for author in authors:
        if author.first_name == first and author.last_name == last:
            author_result = author
            break
    if not author_result.id:
        author_repository.save(author_result)
    book = Book(title, author_result)
    book_repository.save(book)
    return redirect("/books")
