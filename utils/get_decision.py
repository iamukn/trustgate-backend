# gets the fraud decision 

def get_decision(score):
    if score >= 60:
        return "block"
    elif score > 30:
        return "challenge"
    return "allow"
