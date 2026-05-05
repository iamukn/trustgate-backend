from fastapi import APIRouter, status
from schemas.response import PaymentValidationResponse
from schemas.requests import PaymentInfo
from services.trust_engine import evaluate_trust
from fastapi import HTTPException

# router instance
router = APIRouter()


@router.post('/trust/check',
        response_model=PaymentValidationResponse, 
        tags=['TrustGate'], 
        status_code=status.HTTP_200_OK
        )
async def trust_gate(data: PaymentInfo):

    try:
        trust_res = await evaluate_trust(data)
        return trust_res
    except Exception as e:
        raise HTTPException(status_code=500, detail='internal server error')
