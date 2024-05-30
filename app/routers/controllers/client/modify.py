from fastapi import HTTPException, Depends
from app.models.client import ModifyClient
from app.services.db import shark_db

async def modify_client(client_id: int, client: ModifyClient = Depends(ModifyClient.as_form)):

    try:
        client_db = shark_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(client_id,)
        )

        if not client_db:
            raise HTTPException(
                status_code=400,
                detail='User not found'
            )

        update = shark_db.execute(
            sql='UPDATE users SET name = %s, last_name = %s, phone = %s, email = %s WHERE id = %s',
            params=(client.name if client.name is not None else client_db['name'],
                    client.last_name if client.last_name is not None else client_db['last_name'],
                    client.phone if client.phone is not None else client_db['phone'],
                    client.email if client.email is not None else client_db['email'],
                    client_id
                ,)
        )


        


        return {
            'status': 'success',
            'message': 'Worker updated successfully',
            'data': client_db,
            'id': client_db['id'],
            'new_data': {
                'name': client.name if client.name is not None else '',
                'lastname': client.last_name if client.last_name is not None else '',
                'phone': client.phone if client.phone is not None else '',
                'email': client.email if client.email is not None else ''
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error modifying client: {e}"
        )
        