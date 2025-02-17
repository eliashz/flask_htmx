import csv
from sqlalchemy.exc import IntegrityError

from core import db, app
from core.models import Book

def seed_data():
    with app.app_context():
        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book(title=row['Book Name'], author=row['Author Name'])
                db.session.add(book)

            try: 
                db.session.commit()
                print('Books added successfully.')
            except IntegrityError as e:
                db.session.rollback()
                print(f'Error occurred: {e}')

if __name__ == '__main__':
    seed_data()