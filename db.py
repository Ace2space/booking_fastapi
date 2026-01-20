# import psycopg2
#
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="test2",
#         user="amangoyal",
#         password=""
#     )


import os
import psycopg2

def get_connection():
    return psycopg2.connect(os.environ["postgresql://aman:NtAQPvjx6v5Rwoo0o16271UQdbHUrPzN@dpg-d5nm9156ubrc73av76eg-a.singapore-postgres.render.com/booking_db_9g1d"])
