from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def select_all():
    books = []

    sql = 'SELECT * FROM books'
    results = run_sql(sql)

    for dictionary in results:
        author = author_repository.select(dictionary['author_id'])
        book = Book(dictionary['title'], dictionary['genre'], author, dictionary['id'])
        books.append(book)
    return books


def select(id):
    book = None
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    dictionary = run_sql(sql, values)[0]

    if dictionary is not None:
        author = author_repository.select(dictionary['author_id'])
        book = Book(dictionary['title'], dictionary['genre'], author, dictionary['id'])
    return book

def update(book):
    sql = "UPDATE books SET (title, genre, author_id) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)