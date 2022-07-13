from unittest import result
from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(author):
    sql = """INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"""
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = """DELETE FROM authors"""
    run_sql(sql)

def select(id):
    author = None
    sql = """SELECT * FROM authors WHERE id = %s"""
    values = [id]
    results = run_sql(sql, values)[0]
    if result is not None:
        author = Author(results['first_name'], results['last_name'], results['id'])
    return author

def select_all():
    authors = []
    sql = """SELECT * FROM authors ORDER BY id"""
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)
    return authors
