from fastapi import HTTPException, Depends
from app.models.client import Client
from app.services.db import shark_db

async def create_client(client: Client = Depends(Client.as_form)):
    try:
        client_db = shark_db.insert(
            table='users',
            data={
                'name': client.name,
                'last_name': client.last_name,
                'phone': client.phone,
                'email': client.email,
                'permissions_id': 2
            }
        )

        if not client_db:
            raise HTTPException(
                status_code=400,
                detail='Error creating client'
            )
        
        client_date_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(client_db,)
        )

        return {
            'message': 'Client created',
            'client_id': client_db,
            'client_data': client_date_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error creating client: {e}"
        )
    