# calculates the fraud risk

from core.config import MIN_RISK_SCORE, MAX_RISK_SCORE, NUMBERS_VERIFY_SCORE, DEVICE_STATUS_SCORE 

def calculate_risk(sim_swapped: int = 0,
        number_match='',
        device_match=''
        ) -> int:

    res = {
        "simSwap": False,
        "numbersVerification": False,
        "deviceStatus": False,
        "trustScore": MIN_RISK_SCORE,
        "risk_level": "LOW",
        "action": "ALLOW",
        "payment_url": None
            }

    score = MIN_RISK_SCORE

    if sim_swapped:
        res['simSwap'] = True
        score += sim_swapped

    if number_match:
        if number_match.get('devicePhoneNumberVerified'):
            score = score - NUMBERS_VERIFY_SCORE
            res['numbersVerification'] = True
        elif not number_match.get('devicePhoneNumberVerified'):
            score += NUMBERS_VERIFY_SCORE
            res['numbersVerification'] = False

    if device_match:
        is_reachable = device_match.get('reachable')
        if is_reachable:
            score -= DEVICE_STATUS_SCORE
            res['deviceStatus'] = True
        else:
            score += DEVICE_STATUS_SCORE
            res['deviceStatus'] = False

    if score < MIN_RISK_SCORE:
        # normalize the score if it's negative
        score = MIN_RISK_SCORE
    elif score > MAX_RISK_SCORE:
        score = MAX_RISK_SCORE

    res['trustScore'] = score

    res['risk_level'] = 'HIGH' if score >= 43 else 'MEDIUM' if score >= 30 else 'LOW'
    res['action'] = 'BLOCK' if score >= 43 else 'ALLOW'
    return res
