from fastapi import APIRouter, HTTPException
from services.booking_service import (
    create_booking,
    get_booking,
    update_booking,
    cancel_booking
)

router = APIRouter()


@router.post("/bookings", status_code=201)
def create(data: dict):
    booking_id = create_booking(data)
    return {"booking_id": booking_id}


@router.get("/bookings/{booking_id}")
def get(booking_id: int):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.put("/bookings/{booking_id}")
def update(booking_id: int, data: dict):
    update_booking(booking_id, data)
    return {"message": "Booking updated"}


@router.delete("/bookings/{booking_id}")
def cancel(booking_id: int):
    cancel_booking(booking_id)
    return {"message": "Booking cancelled"}

# for frontend:
@router.get("/bookings")
def list_all():
    from services.booking_service import list_bookings
    return list_bookings()

