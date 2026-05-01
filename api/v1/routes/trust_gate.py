from fastapi import APIRouter, status
from schemas.response import PaymentValidationResponse
from schemas.requests import PaymentInfo
from services.trust_engine import evaluate_trust

# router instance
router = APIRouter()


@router.post('/trust/check',
        response_model=PaymentValidationResponse, 
        tags=['TrustGate'], 
        status_code=status.HTTP_200_OK
        )
async def trust_gate(data: PaymentInfo):

    await evaluate_trust(data)
    res = {
            "simSwap": True,
            "numbersVerification": True,
            "deviceStatus": False,
            "trustScore": 45,
            "risk_level": "HIGH",
            "action": "BLOCK"
            #"payment_url": 'https://www.google.com'
            }

    return res
