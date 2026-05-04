import core.config
from core.config import headers
import requests 
import os
from utils.format_to_days import get_days_since_swap
from utils.compute_swap_score_from_days_swapped import compute_new_swap_score_based_on_days


BASE_URL = os.environ.get("BASE_URL")

async def sim_swap(phone: str):

    # swap score
    swap_score = 0

    url = f"{BASE_URL}/passthrough/camara/v1/sim-swap/sim-swap/v0/check"
    
    payload = {
        "phoneNumber": phone,
        "maxAge": 240
            }
    response = requests.post(
            url,
            json=payload,
            headers=headers
            )


    if (response.status_code == 200):
        result = response.json()

        # check if the sim was swapped
        if result.get('swapped'):
            swapped_score = 60
            # Check when it was swapped
            url = f"{BASE_URL}/passthrough/camara/v1/sim-swap/sim-swap/v0/retrieve-date"
            response = requests.post(
                    url,
                    json=payload,
                    headers=headers
                    )

            sim_change_date = response.json().get('latestSimChange')

            if sim_change_date:
                # get number of days swapped
                get_days_swapped = get_days_since_swap(sim_change_date)

                # update the sim swap score
                swap_score = compute_new_swap_score_based_on_days(get_days_swapped)
    return swap_score
