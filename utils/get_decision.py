# gets the fraud decision 
from core.config import BLOCK, CHALLENGE

def get_decision(score):
    if score >= BLOCK:
        return "block"
    elif score > CHALLENGE:
        return "challenge"
    return "allow"
