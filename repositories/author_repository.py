from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING * "
    values = [author.first_name, author.last_name]
    results= run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for dictionary in results:
        author = Author(dictionary['first_name'], dictionary['last_name'], dictionary['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    dictionary = run_sql(sql, values)[0]

    if dictionary is not None:
        author = Author(dictionary['first_name'], dictionary['last_name'], dictionary['id'])
    return author

def update(author):
    sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [author.first_name, author.last_name]
    run_sql(sql, values)
