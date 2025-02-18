from flask import render_template, request
from core import app
from core.models import Book
import math

@app.route('/')
def index():
    books_per_page = 20
    pages = math.ceil(Book.query.count() / books_per_page)
    books = Book.query.paginate(page=1, per_page=books_per_page)
    return render_template('index.html', books=books, pages=pages + 1)

@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        results = Book.query.filter(Book.title.ilike(f'%{query}%') | Book.author.ilike(f'%{query}%')).limit(10).all()
    else:
        results = Book.query.limit(20).all()
    return render_template('search.html', results=results)