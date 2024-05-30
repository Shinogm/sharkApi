from fastapi import HTTPException
from app.services.db import shark_db

async def get_barber(barber_id: int):
    try:
        barber_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(barber_id,)
        )
        if not barber_db:
            raise HTTPException(
                status_code=404,
                detail='Barber not found'
            )

        return {
            'message': 'Barber found',
            'barber': barber_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error getting barber: {e}"
        )
    
async def get_barbers():
    try:
        barbers_db = shark_db.fetch_all(
            sql='SELECT * FROM users WHERE permissions_id = %s',
            params=(1,)
        )
        if not barbers_db:
            raise HTTPException(
                status_code=404,
                detail='Barber not found'
            )
        

        return {
            'message': 'Barbers found',
            'barbers': barbers_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error getting barbers: {e}"
        )