from pydantic import BaseModel
from typing import Optional

class PaymentValidationResponse(BaseModel):
    simSwap: bool
    numbersVerification: bool
    deviceStatus: bool
    trustScore: int
    risk_level: str
    payment_url: Optional[str] = None
