from fastapi import APIRouter
from app.routers.controllers.client.functions import cita

router = APIRouter(prefix="/citas", tags=["citas"] )

router.post('/create/cita/{client_id}/{barber_id}')(cita.create_cita)
router.post('/status/done/{cita_id}')(cita.status_done)
router.get('/get/status/pending')(cita.get_status_pending)