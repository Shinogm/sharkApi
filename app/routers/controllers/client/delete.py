from fastapi import HTTPException
from app.services.db import shark_db

async def delete_client(client_id: int):
    try:
        client_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(client_id,)
        )

        if not client_db:
            raise HTTPException(
                status_code=400,
                detail='Error deleting client'
            )

        delete = shark_db.execute(
            sql='DELETE FROM users WHERE id = %s',
            params=(client_id,)
        )

        if not client_db:
            raise HTTPException(
                status_code=400,
                detail='Error deleting client'
            )
        
        return {
            'message': 'Client deleted',
            'client_id': delete,
            'client_data': client_db
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error deleting client: {e}"
        )