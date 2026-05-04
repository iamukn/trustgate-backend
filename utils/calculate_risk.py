# calculates the fraud risk
def calculate_risk(sim_swapped: int = 0,
        number_match='',
        device_match=''
        ) -> int:

    res = {
        "simSwap": False,
        "numbersVerification": False,
        "deviceStatus": False,
        "trustScore": 0,
        "risk_level": "LOW",
        "action": "ALLOW",
        "payment_url": None
            }

    score = 0

    print('SS: ', sim_swapped)
    if sim_swapped:
        res['simSwap'] = True
        score += sim_swapped

    if number_match:
        if number_match.get('devicePhoneNumberVerified'):
            score = score - 30
            res['numbersVerification'] = True
        elif not number_match.get('devicePhoneNumberVerified'):
            score += 30
            res['numbersVerification'] = False

    if device_match:
        is_reachable = device_match.get('reachable')
        if is_reachable:
            score -= 15
            res['deviceStatus'] = True
        else:
            score += 15
            res['deviceStatus'] = False

    if score < 0:
        # normalize the score if it's negative
        score = 0
    elif score > 100:
        score = 100

    res['trustScore'] = score

    res['risk_level'] = 'HIGH' if score >= 43 else 'MEDIUM' if score >= 30 else 'LOW'
    res['action'] = 'BLOCK' if score >= 43 else 'ALLOW'
    return res
