from fastapi import HTTPException, Depends
from app.models.barber import Barber
from app.services.db import shark_db
import bcrypt
async def create_barber(barber: Barber = Depends(Barber.as_form)):
    try:
        barber_db = shark_db.insert(
            table='users',
            data={
                'name': barber.name,
                'last_name': barber.last_name,
                'phone': barber.phone,
                'email': barber.email,
                'password': bcrypt.hashpw(barber.password.encode('utf-8'), bcrypt.gensalt())
            }
        )

        if not barber_db:
            raise HTTPException(
                status_code=400,
                detail='Error creating barber'
            )
        
        barber_date_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(barber_db,)
        )

        return {
            'message': 'Barber created',
            'barber_id': barber_db,
            'barber_data': barber_date_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error creating barber: {e}"
        )