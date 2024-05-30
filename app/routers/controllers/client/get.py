from fastapi import HTTPException, Depends
from app.services.db import shark_db

async def get_client(client_id: int):

    try:
        client_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(client_id,)
        )

        if not client_db:
            raise HTTPException(
                status_code=400,
                detail='Error getting client'
            )
        

        return {
            'message': 'Client retrieved',
            'client_id': client_id,
            'client_data': client_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error getting client: {e}"
        )

async def get_clients():

    try:
        clients_db = shark_db.fetch_all(
            sql='SELECT * FROM users WHERE permissions_id = %s',
            params=(2,)
        )

        if not clients_db:
            raise HTTPException(
                status_code=400,
                detail='Error getting clients'
            )
        

        return {
            'message': 'Clients retrieved',
            'clients_id': clients_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error getting clients: {e}"
        )
