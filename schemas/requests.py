from pydantic import BaseModel, EmailStr
from typing import Optional


class PaymentInfo(BaseModel):
    phone: str
    amount: Optional[float]
    email: Optional[EmailStr] = None
    name: Optional[str]=None
