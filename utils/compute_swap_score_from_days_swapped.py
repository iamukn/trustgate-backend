from core.config import MIN_RISK_SCORE, SIXTY, TWENTY, FIFTY_EIGHT, FIFTY, FOURTY, TWENTY

def compute_new_swap_score_based_on_days(days: float):

    score = MIN_RISK_SCORE

    days = int(days)
    
    if days == 0:
        score = SIXTY

    elif days == 1:
        score = FIFTY_EIGHT

    elif days >= 2 and days <= 5:
        score = FIFTY

    elif days >= 6 and days <= 10:
        score = FOURTY

    elif days >= 11 and days <= 20:
        score = TWENTY

    else:
        score = MIN_RISK_SCORE

    return score
