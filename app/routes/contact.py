from fastapi import APIRouter
from app.models import Contact
from app.services.dynamodb import save_contact
from app.services.sqs import send_event

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/")
def contact_form(payload: Contact):

    data = payload.dict()

    save_contact(data)

    send_event({
        "type": "CONTACT_MESSAGE",
        "data": data
    })

    return {"message": "Message received"}
