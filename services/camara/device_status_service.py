#!/usr/bin/python3
import core.config
from core.config import headers

import os
import requests

BASE_URL = os.environ.get('BASE_URL')

async def device_status(phoneNumber: str) -> int:

    risk_score = 0

    payload = {
            "device": {"phoneNumber": phoneNumber}
            }

    url = f"{BASE_URL}/device-status/v0/connectivity"
    # request to the device status api 
    response = requests.post(
            url,
            json=payload,
            headers=headers
        )

    if (response.status_code == 200):

        status = response.json().get('connectivityStatus')

        if (status.upper() == 'CONNECTED_DATA' or status.upper() == 'CONNECTED_SMS'):
            risk_score = 0
        else:
            risk_score += 15

    return risk_score
