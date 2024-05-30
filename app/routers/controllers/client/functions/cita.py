from fastapi import HTTPException
from app.services.db import shark_db
from datetime import date, time

async def create_cita(client_id: int, barber_id: int, dia: date, hora: str):
    try:
        get_client = shark_db.fetch_one(
            sql="SELECT * FROM users WHERE id = %s",
            params=[client_id]
        )

        if not get_client or get_client['permissions_id'] != 2:
            raise HTTPException(status_code=404, detail="Cliente not found")
        
        get_barber = shark_db.fetch_one(
            sql="SELECT * FROM users WHERE id = %s",
            params=[barber_id]
        )

        if not get_barber or get_barber['permissions_id'] != 1:
            raise HTTPException(status_code=404, detail="Barber not found")
        
        get_cita = shark_db.fetch_one(
            sql="SELECT * FROM citas WHERE cliente_id = %s AND status = 'pending'",
            params=[client_id]
        )

        if get_cita:
            raise HTTPException(status_code=400, detail="Cliente already has a pending cita")

        cita_id = shark_db.execute(
            sql="INSERT INTO citas (dia, hora, barber_id, cliente_id) VALUES (%s, %s, %s, %s)",
            params=[dia, hora, barber_id, client_id]
        )

        if not cita_id:
            raise HTTPException(status_code=500, detail="Error creating cita")
        
        get_cita = shark_db.fetch_one(
            sql="SELECT * FROM citas WHERE id = %s",
            params=[cita_id]
        )
        
        return {
            'created_at': get_cita['created_at'],
            'status': get_cita['status'],
            "id": get_cita["id"],
            "dia": get_cita["dia"],
            "hora": get_cita["hora"],
            "barber": get_barber,
            "cliente": get_client
        }
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating cita {e}')


async def status_done(cita_id: int):
    try:
        get_cita = shark_db.fetch_one(
            sql="SELECT * FROM citas WHERE id = %s",
            params=[cita_id]
        )

        if not get_cita:
            raise HTTPException(status_code=404, detail="Cita not found")

        if get_cita['status'] == 'done' or get_cita['status'] == 'canceled':
            raise HTTPException(status_code=400, detail="Cita already done or canceled")

        shark_db.execute(
            sql="UPDATE citas SET status = 'done' WHERE id = %s",
            params=[cita_id]
        )

        get_new_cita = shark_db.fetch_one(
            sql="SELECT * FROM citas WHERE id = %s",
            params=[cita_id]
        )

        get_ciente = shark_db.fetch_one(
            sql="SELECT * FROM users WHERE id = %s",
            params=[get_new_cita['cliente_id']]
        )

        get_barber = shark_db.fetch_one(
            sql="SELECT * FROM users WHERE id = %s",
            params=[get_new_cita['barber_id']]
        )

        return {
            'status': get_new_cita['status'],
            "id_cita": get_cita["id"],
            'cliente': get_ciente,
            'barber': get_barber
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating status {e}')
    
async def get_status_pending():
    try:
        get_citas = shark_db.fetch_all(
            sql='''
                    SELECT
                        c.id AS cita_id,
                        c.dia,
                        c.hora,
                        c.status,
                            cliente.id AS cliente_id,
                            cliente.name AS cliente_name,
                            cliente.last_name AS cliente_last_name,
                            cliente.phone AS cliente_phone,
                            cliente.email AS cliente_email,
                        barber.id AS barber_id,
                        barber.name AS barber_name,
                        barber.last_name AS barber_last_name,
                        barber.phone AS barber_phone,
                        barber.email AS barber_email
                    FROM 
                        citas c
                    JOIN 
                        users cliente ON c.cliente_id = cliente.id
                    JOIN 
                        users barber ON c.barber_id = barber.id
                    WHERE 
                        c.status = 'pending'
                        '''
        )

        if not get_citas:
            raise HTTPException(status_code=404, detail="Citas not found")
        

        return {
            'status_pending': get_citas,
        }
            

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error getting status pending {e}')