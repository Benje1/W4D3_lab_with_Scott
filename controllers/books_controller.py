from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repository

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("/books/index.html", all_books = books)