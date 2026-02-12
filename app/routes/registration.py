from fastapi import APIRouter
from app.models import Registration
from app.services.dynamodb import save_registration
from app.services.sqs import send_event

router = APIRouter(prefix="/registration", tags=["Registration"])

@router.post("/")
def register_user(payload: Registration):

    data = payload.dict()

    # Save to DynamoDB
    save_registration(data)

    # Send async event to SQS
    send_event({
        "type": "NEW_REGISTRATION",
        "data": data
    })

    return {"message": "Registration successful"}
