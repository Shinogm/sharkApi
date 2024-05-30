from fastapi import APIRouter
from app.routers.controllers.barber import create, get
from app.utils.login import verify_password

router = APIRouter(prefix='/barber', tags=['barber'])

router.post('/create')(create.create_barber)
router.post('/login')(verify_password)
router.get('/get')(get.get_barbers)
router.get('/get/{barber_id}')(get.get_barber)