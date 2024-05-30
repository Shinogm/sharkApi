from fastapi import APIRouter
from app.routers.controllers.client import create, get, modify, delete

router = APIRouter(prefix='/client', tags=['client'])

router.post('/create')(create.create_client)
router.get('/get')(get.get_clients)
router.get('/get/{client_id}')(get.get_client)
router.patch('/modify/{client_id}')(modify.modify_client)
router.delete('/delete/{client_id}')(delete.delete_client)

