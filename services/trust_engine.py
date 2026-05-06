#!/usr/bin/python3
from utils.get_decision import get_decision
from services.camara.sim_swap_service import sim_swap
from services.camara.device_status_service import device_status
from services.camara.numbers_verification_service import number_verify
from utils.calculate_risk import calculate_risk


async def evaluate_trust(data):
    phone=data.phone
    # Verify if the sim has been swapped and score it
    sim_swap_risk = await sim_swap(phone)
    device_status_reachability = await device_status(phone)

    # calculate fraud_risk_score
    confidence = calculate_risk(sim_swapped=sim_swap_risk,
            device_match=device_status_reachability
            )
    
    # Add an extra verification layer if the risk score >=43
    if (confidence.get('trustScore') >= 43):
        # call number api
        number_verify_risk = await number_verify(phone)
        # recalculate_confidence
        confidence = calculate_risk(sim_swapped=sim_swap_risk,
                device_match=device_status_reachability,
                number_match=number_verify_risk
                )

    return confidence
