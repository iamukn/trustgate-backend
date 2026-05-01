#!/usr/bin/python3
from utils.get_decision import get_decision
from services.camara.sim_swap_service import sim_swap
from services.camara.device_status_service import device_status


# calculates the fraud risk
def calculate_risk(sim_swapped: int = 0, 
        number_match: int = 0, 
        device_match: int = 0
        ) -> int:

    score = 0

    if sim_swapped:
        score += sim_swapped

    if number_match:
        score -= number_match

    if device_match:
        score -= device_match

    return score


async def evaluate_trust(data):

    phone=data.phone

    # Verify if the sim has been swapped and score it
    sim_swap_risk = await sim_swap(phone)
    device_status_risk = await device_status(phone)

    # calculate fraud_risk_score
    confidence = calculate_risk(sim_swapped=sim_swap_risk,
            device_match=device_status_risk
            )
    print(sim_swap_risk, device_status_risk, 'Confidence: ', confidence)
