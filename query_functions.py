

from db import get_db
from sqlalchemy import text


def get_rentals_by_month_and_week(year, month):
    with get_db() as db:
        query = text("""
            SELECT WEEK(created_at) AS week_number, COUNT(*) AS num_rentals
            FROM rental_transactions
            WHERE YEAR(created_at) = :year AND MONTH(created_at) = :month
            GROUP BY WEEK(created_at);
            """)
        result = db.execute(query, {'year': year, 'month': month})
        return result.fetchall()


def get_rentals_by_day(year, month):
    with get_db() as db:
        query = text("""
            SELECT DAY(created_at) AS day, COUNT(*) AS num_rentals
            FROM rental_transactions
            WHERE YEAR(created_at) = :year AND MONTH(created_at) = :month
            GROUP BY DAY(created_at);
            """)
        result = db.execute(query, {'year': year, 'month': month})
        return result.fetchall()

def get_rentals_by_year(year):
    with get_db() as db:
        query = text("""
            SELECT MONTH(created_at) AS month, COUNT(*) AS num_rentals
            FROM rental_transactions
            WHERE YEAR(created_at) = :year
            GROUP BY MONTH(created_at);
            """)
        result = db.execute(query, {'year': year})
        return result.fetchall()

def get_top_rented_items_all_time():
    with get_db() as db:
        query = text("""
        SELECT r.rental_items_id, i.name, COUNT(*) AS num_rentals
        FROM rental_transactions r
        JOIN rental_items i ON r.rental_items_id = i.id
        GROUP BY r.rental_items_id, i.name
        ORDER BY num_rentals DESC
        LIMIT 10;
        """)
        result = db.execute(query)
        return result.fetchall()

def get_top_rented_items_by_year_and_month(year):
    with get_db() as db:
        query = text("""
        SELECT MONTH(r.created_at) AS month, i.name, COUNT(*) AS num_rentals
        FROM rental_transactions r
        JOIN rental_items i ON r.rental_items_id = i.id
        WHERE YEAR(r.created_at) = :year
        GROUP BY MONTH(r.created_at), i.name
        ORDER BY month, num_rentals DESC
        LIMIT 10;
        """)
        result = db.execute(query, {'year': year})
        return result.fetchall()

def get_month_most_items_added(year):
    with get_db() as db:
        query = text("""
            SELECT MONTH(created_at) AS month, COUNT(*) AS num_items
            FROM rental_items
            WHERE YEAR(created_at) = :year
            GROUP BY MONTH(created_at)
            ORDER BY num_items DESC
            LIMIT 1;
            """)
        result = db.execute(query, {'year': year})
        return result.fetchall()