from db import get_connection

def create_booking(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO bookings2 (user_name, hotel_name, check_in, check_out)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (
            data["user_name"],
            data["hotel_name"],
            data["check_in"],
            data["check_out"]
        )
    )

    booking_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return booking_id

def get_booking(booking_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, user_name, hotel_name, status FROM bookings2 WHERE id = %s",
        (booking_id,)
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    return {
        "id": row[0],
        "user_name": row[1],
        "hotel_name": row[2],
        "status": row[3]
    }

def update_booking(booking_id, data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE bookings2
        SET hotel_name = %s,
            check_in = %s,
            check_out = %s
        WHERE id = %s
        """,
        (
            data["hotel_name"],
            data["check_in"],
            data["check_out"],
            booking_id
        )
    )

    conn.commit()
    cur.close()
    conn.close()

def cancel_booking(booking_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE bookings2
        SET status = 'CANCELLED'
        WHERE id = %s
        """,
        (booking_id,)
    )

    conn.commit()
    cur.close()
    conn.close()

# for frontend:
def list_bookings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, user_name, hotel_name, status
        FROM bookings2
        ORDER BY id DESC
        """
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "id": r[0],
            "user_name": r[1],
            "hotel_name": r[2],
            "status": r[3]
        }
        for r in rows
    ]


