from flask import Flask, render_template, request, redirect, Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors = authors)

@books_blueprint.route("/books", methods=['POST'])
def add_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id   = request.form['author_id']
    author = author_repository.select(author_id)
    new_book = Book(title, genre, author)
    book_repository.save(new_book)
    return redirect('/books')

@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, authors = authors)

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    author_id   = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, author, id)
    book_repository.update(book)
    return redirect('/books')


